from flask import Blueprint, render_template

from resource.models import Region

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    regions = Region.query.all()
    return render_template('base.html', regions=regions)
