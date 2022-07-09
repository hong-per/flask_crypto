from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.utils import redirect
from resource import db
from resource.models import Region, Server, Usage
from resource.forms import UsageForm
from datetime import datetime


bp = Blueprint('usage', __name__, url_prefix='/usage')


@bp.route('create/region<int:region_id>', methods=('GET', 'POST'))
def create(region_id):
    region = Region.query.get_or_404(region_id)
    servers = region.servers

    date = request.args.get('record_date')[:10].split('-')
    record_date = datetime(int(date[0]), int(date[1]), int(date[2]), 0, 0)

    form = UsageForm()

    if request.method == 'POST' and form.validate_on_submit():
        for server in servers:
            usage = Usage(
                server_id=server.id,
                cpu_usage=form.cpu_usage.data,
                memory_usage=form.memory_usage.data,
                storage_usage=form.storage_usage.data,
                record_date=record_date
            )
            db.session.add(usage)
        db.session.commit()

        return redirect(url_for('region.detail', region_id=region_id))

    return render_template('usage/add_usage.html', region=region, servers=servers, record_date=record_date, form=form, date=date)
