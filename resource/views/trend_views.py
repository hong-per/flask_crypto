from flask import Blueprint, render_template
from resource.models import Region
import pandas as pd
import json
import plotly
import plotly.express as px

bp = Blueprint('trend', __name__, url_prefix='/trend')


@bp.route('/<int:region_id>/', methods=["GET"])
def main(region_id):
    regions = Region.query.all()
    region = Region.query.get_or_404(region_id)

    line = {
        'cpu': json.dumps(get_cpu_usages_by_dates(region), cls=plotly.utils.PlotlyJSONEncoder),
        'memory': json.dumps(get_memory_usages_by_dates(region), cls=plotly.utils.PlotlyJSONEncoder),
        'storage': json.dumps(get_storage_usages_by_dates(region), cls=plotly.utils.PlotlyJSONEncoder)
    }

    return render_template('trend/trend.html', regions=regions, region=region, line=line)


def get_cpu_usages_by_dates(region):
    df = pd.DataFrame({
        'date': region.dates(),
        'usage': region.cpu_usage_by_date()
    })
    return px.line(df, x="date", y="usage", title=f"cpu usage trend in {region.name}")


def get_memory_usages_by_dates(region):
    df = pd.DataFrame({
        'date': region.dates(),
        'usage': region.memory_usage_by_date()
    })
    return px.line(df, x="date", y="usage", title=f"memory usage trend in {region.name}")


def get_storage_usages_by_dates(region):
    df = pd.DataFrame({
        'date': region.dates(),
        'usage': region.storage_usage_by_date()
    })
    return px.line(df, x="date", y="usage", title=f"storage usage trend in {region.name}")
