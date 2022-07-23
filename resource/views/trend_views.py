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
    logs = sum([server.logs for server in region.servers], [])
    dates = list(set([log.record_date for log in logs]))
    dates.sort()

    df = pd.DataFrame({
        'date': dates,
        'usage': [5, 6, 7, 8, 10, 12]
    })
    fig = px.line(df, x="date", y="usage", title='usage trend by date')
    graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('trend/trend.html', regions=regions, region=region, graph=graph)
