from flask import Blueprint, render_template

from resource.models import Region

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    region_list = Region.query.order_by(Region.name.desc())
    return render_template('region/region_list.html', region_list=region_list)
