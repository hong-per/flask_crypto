from flask import Blueprint, url_for, render_template, flash, request

from resource.models import Region, Server, Usage

bp = Blueprint('region', __name__, url_prefix='/region')


# @bp.route('/<int:region_id>/')
# def region(region_id):
#     regions = Region.query.all()
#     target_region = Region.query.get_or_404(region_id)
#     return render_template('region/region_detail.html', regions=regions, target_region=target_region)
