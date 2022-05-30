from flask import Blueprint, url_for, render_template, flash, request

from resource.models import Region, Server, Usage

bp = Blueprint('region', __name__, url_prefix='/region')


@bp.route('/<int:region_id>/')
def region(region_id):
    regions = Region.query.all()
    region = Region.query.get_or_404(region_id)
    servers = Server.query.filter_by(region_id=region_id)
    return render_template('region/region_detail.html', regions=regions, region=region, servers=servers)
