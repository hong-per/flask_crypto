from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.utils import redirect
from resource import db
from resource.models import Region, Server, Usage
from resource.forms import UsageForm
from datetime import datetime


bp = Blueprint('usage', __name__, url_prefix='/usage')


@bp.route('create/region<int:region_id>', methods=('GET', 'POST'))
def create(region_id):
    region = region_id
    # date = request.args.get('record_date')[:10].split('-')
    # record_date = datetime(int(date[0]), int(date[1]), int(date[2]), 0, 0)
    record_date = request.args.get('record_date')

    # form = UsageForm()
    # region = Region.query.get_or_404(region_id)

    # if request.method == 'POST' and form.validate_on_submit():
    #     server = Server(region_id=region_id, host=form.host.data, cpu=form.cpu.data,
    #                     memory=form.memory.data, storage=form.storage.data)
    #     db.session.add(server)
    #     db.session.commit()
    #     return redirect(url_for('region.detail', region_id=region_id))

    return render_template('usage/add_usage.html', region=region, record_date=record_date)


# @bp.route('update/<int:server_id>/', methods=('GET', 'POST'))
# def update(server_id):
#     form = ServerForm()
#     server = Server.query.get_or_404(server_id)
#     region_id = server.region_id

#     if request.method == 'POST' and form.validate_on_submit():
#         server.host = form.host.data
#         server.cpu = form.cpu.data
#         server.memory = form.memory.data
#         server.storage = form.storage.data
#         db.session.commit()
#         return redirect(url_for('region.detail', region_id=region_id))

#     return render_template('server/update_server.html', server=server, form=form)
