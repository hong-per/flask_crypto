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
    df = pd.DataFrame({
        'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
                  'Bananas'],
        'Amount': [4, 1, 2, 2, 4, 5],
        'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    })

    fig = px.bar(df, x='Fruit', y='Amount', color='City',
                 barmode='group')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', regions=regions, graphJSON=graphJSON)
