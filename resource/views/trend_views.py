from flask import Blueprint, render_template
from resource.models import Region
import pandas as pd
import json
import plotly
import plotly.express as px
from functools import reduce

bp = Blueprint('trend', __name__, url_prefix='/trend')


@bp.route('/<int:region_id>/', methods=["GET"])
def main(region_id):
    regions = Region.query.all()
    region = Region.query.get_or_404(region_id)

    df = pd.DataFrame({
        'date': [1, 2, 3, 4],
        'usage': [5, 6, 7, 8]
    })
    fig = px.line(df, x="date", y="usage", title='usage trend by date')
    graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('trend/trend.html', regions=regions, region=region, graph=graph)
