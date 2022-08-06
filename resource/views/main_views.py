from flask import Blueprint, render_template
from resource.models import Region
import pandas as pd
import json
import plotly
import plotly.express as px
from functools import reduce

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    regions = Region.query.all()
    usage = {}

    for region in regions:
        usage[region.name] = {}
        usage[region.name]['cpu'] = json.dumps(get_cpu_pie_by_region(
            region), cls=plotly.utils.PlotlyJSONEncoder)
        usage[region.name]['memory'] = json.dumps(get_memory_pie_by_region(
            region), cls=plotly.utils.PlotlyJSONEncoder)
        usage[region.name]['storage'] = json.dumps(
            get_storage_pie_by_region(region), cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', regions=regions, usage=usage)


def get_cpu_pie_by_region(region):
    df = pd.DataFrame({
        'usage': [region.cpu_usage(), (region.total_cpu() - region.cpu_usage())],
        'name': [f"{region}_cpu_usage", f"{region}_cpu_remain"]
    })

    return px.pie(df, values="usage", names="name", title=f"{region} cpu usage")


def get_memory_pie_by_region(region):
    df = pd.DataFrame({
        'usage': [region.memory_usage(), (region.total_memory() - region.memory_usage())],
        'name': [f"{region}_memory_usage", f"{region}_memory_remain"]
    })

    return px.pie(df, values="usage", names="name", title=f"{region} memory usage")


def get_storage_pie_by_region(region):
    df = pd.DataFrame({
        'usage': [region.storage_usage(), (region.total_storage() - region.storage_usage())],
        'name': [f"{region}_storage_usage", f"{region}_storage_remain"]
    })

    return px.pie(df, values="usage", names="name", title=f"{region} storage usage")
