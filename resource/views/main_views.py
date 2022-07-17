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

    east = Region.query.filter_by(name='east').first()
    logs = sum([server.logs for server in east.servers], [])
    recent_date = max(log.record_date for log in logs)
    recent_logs = list(filter(lambda x: x.record_date == recent_date, logs))

    cpu_usage_sum = reduce(
        lambda x, y: x + y, [log.cpu_usage for log in recent_logs])
    memory_usage_sum = reduce(
        lambda x, y: x + y, [log.memory_usage for log in recent_logs])
    storage_usage_sum = reduce(
        lambda x, y: x + y, [log.cpu_usage for log in recent_logs])

    cpu_sum = reduce(lambda x, y: x + y,
                     [server.cpu for server in east.servers])
    memory_sum = reduce(lambda x, y: x + y,
                        [server.memory for server in east.servers])
    storage_sum = reduce(lambda x, y: x + y,
                         [server.storage for server in east.servers])

    # CPU
    df = pd.DataFrame({
        'usage': [cpu_usage_sum, (cpu_sum - cpu_usage_sum)],
        'name': ['east_cpu_usage', 'east_cpu_remain']
    })

    cpu = px.pie(df, values="usage", names="name", title="cpu usage")

    CPU = json.dumps(cpu, cls=plotly.utils.PlotlyJSONEncoder)

    # Memory
    df = pd.DataFrame({
        'usage': [memory_usage_sum, (memory_sum - memory_usage_sum)],
        'name': ['east_memory_usage', 'east_memory_remain']
    })

    memory = px.pie(df, values="usage", names="name", title="memory usage")

    MEMORY = json.dumps(memory, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', regions=regions, CPU=CPU, MEMORY=MEMORY)
