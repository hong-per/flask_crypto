from flask import Blueprint, render_template
from resource.models import Region
import pandas as pd
import json
import plotly
import plotly.express as px

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    regions = Region.query.all()

    # Graph One
    # df = pd.DataFrame({
    #     'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
    #               'Bananas'],
    #     'Amount': [4, 1, 2, 2, 4, 5],
    #     'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    # })

    # fig1 = px.bar(df, x='Fruit', y='Amount', color='City',
    #               barmode='group')

    # graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    east = Region.query.filter_by(name='east').first()
    east_logs = [server.logs for server in east.servers]
    dates = [log.record_date for log in east_logs[0]]
    recent_date = max(dates)
    # Graph Two
    df = pd.DataFrame({
        'usage': [80, 20],
        'name': ['east_1_usage', 'east_1_remain']
    })

    fig2 = px.pie(df, values="usage", names="name", title="server usage")

    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph Three
    df = pd.DataFrame({
        'usage': [50, 50],
        'name': ['west_1_usage', 'west_1_remain']
    })

    fig3 = px.pie(df, values="usage", names="name", title="server usage")

    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', regions=regions, graph2JSON=graph2JSON, graph3JSON=graph3JSON)
