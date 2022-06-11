from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.utils import redirect
from resource import db
from resource.models import Region, Server, Usage
from resource.forms import DateForm

from datetime import date, datetime

bp = Blueprint('region', __name__, url_prefix='/region')


@bp.route('/<int:region_id>/', methods=('GET', 'POST'))
def detail(region_id):
    regions = Region.query.all()
    region = Region.query.get_or_404(region_id)

    page = request.args.get('page', type=int, default=1)
    servers = Server.query.filter_by(region_id=region_id)
    servers = servers.paginate(page, per_page=10)

    form = DateForm()

    if request.method == 'GET' and form.validate_on_submit():
        date = form.date.data
        usages = Usage.query.filter_by(record_date=date)
        if usages:
            flash(f'Record usages for {date}')
        else:
            flash(f'There is no record for {date}')

    return render_template('region/region_detail.html', regions=regions, region=region, servers=servers, form=form)
