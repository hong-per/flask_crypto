from flask import Blueprint, render_template
from resource.models import Region
import pandas as pd
import json
import plotly
import plotly.express as px
from functools import reduce
from datetime import datetime

bp = Blueprint('trend', __name__, url_prefix='/trend')


@bp.route('/<int:region_id>/', methods=["GET"])
def main(region_id):
    regions = Region.query.all()
    region = Region.query.get_or_404(region_id)

    line = {
        'cpu': json.dumps(get_cpu_usages_by_dates(region),
                          cls=plotly.utils.PlotlyJSONEncoder),
        'memory': json.dumps(get_memory_usages_by_dates(region),
                             cls=plotly.utils.PlotlyJSONEncoder),
        'storage': json.dumps(get_storage_usages_by_dates(region),
                              cls=plotly.utils.PlotlyJSONEncoder)
    }

    return render_template('trend/trend.html', regions=regions, region=region, line=line)


def get_logs_by_region(region):
    return sum([server.logs for server in region.servers], [])


def get_dates_by_region(region):
    logs = get_logs_by_region(region)
    return list(set([log.record_date for log in logs]))


def get_cpu_usages_by_dates(region):
    logs = get_logs_by_region(region)
    dates = get_dates_by_region(region)
    dates.sort()

    cpu_usages = []
    for date in dates:
        date_logs = list(filter(lambda x: x.record_date == date, logs))
        cpu_usages.append(
            reduce(lambda x, y: x + y, [log.cpu_usage for log in date_logs]))

    df = pd.DataFrame({
        'date': dates,
        'usage': cpu_usages
    })
    return px.line(df, x="date", y="usage", title=f"cpu usage trend by date in {region.name}")


def get_memory_usages_by_dates(region):
    logs = get_logs_by_region(region)
    dates = get_dates_by_region(region)
    dates.sort()

    memory_usages = []
    for date in dates:
        date_logs = list(filter(lambda x: x.record_date == date, logs))
        memory_usages.append(
            reduce(lambda x, y: x + y, [log.memory_usage for log in date_logs]))

    df = pd.DataFrame({
        'date': dates,
        'usage': memory_usages
    })
    return px.line(df, x="date", y="usage", title=f"memory usage trend by date in {region.name}")


def get_storage_usages_by_dates(region):
    logs = get_logs_by_region(region)
    dates = get_dates_by_region(region)
    dates.sort()

    storage_usages = []
    for date in dates:
        date_logs = list(filter(lambda x: x.record_date == date, logs))
        storage_usages.append(
            reduce(lambda x, y: x + y, [log.storage_usage for log in date_logs]))

    df = pd.DataFrame({
        'date': dates,
        'usage': storage_usages
    })
    return px.line(df, x="date", y="usage", title=f"storage usage trend by date in {region.name}")
