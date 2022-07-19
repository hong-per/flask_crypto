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

    east_cpu_pie = json.dumps(
        get_cpu_pie_by_region('east'),
        cls=plotly.utils.PlotlyJSONEncoder
    )
    east_memory_pie = json.dumps(
        get_memory_pie_by_region('east'),
        cls=plotly.utils.PlotlyJSONEncoder
    )
    east_storage_pie = json.dumps(
        get_storage_pie_by_region('east'),
        cls=plotly.utils.PlotlyJSONEncoder
    )

    west_cpu_pie = json.dumps(
        get_cpu_pie_by_region('west'),
        cls=plotly.utils.PlotlyJSONEncoder
    )
    west_memory_pie = json.dumps(
        get_memory_pie_by_region('west'),
        cls=plotly.utils.PlotlyJSONEncoder
    )
    west_storage_pie = json.dumps(
        get_storage_pie_by_region('west'),
        cls=plotly.utils.PlotlyJSONEncoder
    )

    south_cpu_pie = json.dumps(
        get_cpu_pie_by_region('south'),
        cls=plotly.utils.PlotlyJSONEncoder
    )
    south_memory_pie = json.dumps(
        get_memory_pie_by_region('south'),
        cls=plotly.utils.PlotlyJSONEncoder
    )
    south_storage_pie = json.dumps(
        get_storage_pie_by_region('south'),
        cls=plotly.utils.PlotlyJSONEncoder
    )

    north_cpu_pie = json.dumps(
        get_cpu_pie_by_region('north'),
        cls=plotly.utils.PlotlyJSONEncoder
    )
    north_memory_pie = json.dumps(
        get_memory_pie_by_region('north'),
        cls=plotly.utils.PlotlyJSONEncoder
    )
    north_storage_pie = json.dumps(
        get_storage_pie_by_region('north'),
        cls=plotly.utils.PlotlyJSONEncoder
    )

    return render_template(
        'dashboard.html', regions=regions,
        east_cpu_pie=east_cpu_pie, east_memory_pie=east_memory_pie, east_storage_pie=east_storage_pie,
        west_cpu_pie=west_cpu_pie, west_memory_pie=west_memory_pie, west_storage_pie=west_storage_pie,
        south_cpu_pie=south_cpu_pie, south_memory_pie=south_memory_pie, south_storage_pie=south_storage_pie,
        north_cpu_pie=north_cpu_pie, north_memory_pie=north_memory_pie, north_storage_pie=north_storage_pie
    )


def get_recent_logs_by_region(region):
    target = Region.query.filter_by(name=region).first()
    logs = sum([server.logs for server in target.servers], [])
    recent_date = max(log.record_date for log in logs)
    return list(filter(lambda x: x.record_date == recent_date, logs))


def get_cpu_pie_by_region(region):
    target = Region.query.filter_by(name=region).first()
    recent_logs = get_recent_logs_by_region(region)

    cpu_usage = reduce(lambda x, y: x + y,
                       [log.cpu_usage for log in recent_logs])

    total_cpu = reduce(lambda x, y: x + y,
                       [server.cpu for server in target.servers])

    df = pd.DataFrame({
        'usage': [cpu_usage, (total_cpu - cpu_usage)],
        'name': [f"{region}_cpu_usage", f"{region}_cpu_remain"]
    })

    return px.pie(df, values="usage", names="name", title=f"{region} cpu usage")


def get_memory_pie_by_region(region):
    target = Region.query.filter_by(name=region).first()
    recent_logs = get_recent_logs_by_region(region)

    memory_usage = reduce(lambda x, y: x + y,
                          [log.memory_usage for log in recent_logs])

    total_memory = reduce(lambda x, y: x + y,
                          [server.memory for server in target.servers])

    df = pd.DataFrame({
        'usage': [memory_usage, (total_memory - memory_usage)],
        'name': [f"{region}_memory_usage", f"{region}_memory_remain"]
    })

    return px.pie(df, values="usage", names="name", title=f"{region} memory usage")


def get_storage_pie_by_region(region):
    target = Region.query.filter_by(name=region).first()
    recent_logs = get_recent_logs_by_region(region)

    storage_usage = reduce(lambda x, y: x + y,
                           [log.storage_usage for log in recent_logs])

    total_storage = reduce(lambda x, y: x + y,
                           [server.storage for server in target.servers])

    df = pd.DataFrame({
        'usage': [storage_usage, (total_storage - storage_usage)],
        'name': [f"{region}_storage_usage", f"{region}_storage_remain"]
    })

    return px.pie(df, values="usage", names="name", title=f"{region} storage usage")
