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
    df = pd.DataFrame({
        'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
                  'Bananas'],
        'Amount': [4, 1, 2, 2, 4, 5],
        'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    })

    fig1 = px.bar(df, x='Fruit', y='Amount', color='City',
                  barmode='group')

    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph Two
    df = pd.DataFrame({
        'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
                  'Bananas'],
        'Amount': [14, 11, 12, 12, 14, 15],
        'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    })

    # fig2 = px.bar(df, x='Fruit', y='Amount', color='City',
    #               barmode='group')
    fig2 = px.scatter(df, x="Fruit", y="Amount", color="City",
                      #   size="population", color="continent", hover_name="country",
                      log_x=True, size_max=60)

    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', regions=regions, graph1JSON=graph1JSON, graph2JSON=graph2JSON)
