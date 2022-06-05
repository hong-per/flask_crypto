from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.utils import redirect
from resource import db
from resource.models import Region, Server, Usage
from resource.forms import ServerForm

bp = Blueprint('server', __name__, url_prefix='/server')


@bp.route('update/<int:server_id>/', methods=('GET', 'POST'))
def update(server_id):
    form = ServerForm()
    server = Server.query.get_or_404(server_id)
    region_id = server.region_id

    if request.method == 'POST' and form.validate_on_submit():
        server.host = form.host.data
        server.cpu = form.cpu.data
        server.memory = form.memory.data
        server.instance = form.instance.data
        db.session.commit()
        return redirect(url_for('region.detail', region_id=region_id))

    return render_template('server/update_server.html', server=server, form=form)


@bp.route('delete/<int:server_id>/', methods=('GET', 'POST'))
def delete(server_id):
    server = Server.query.get_or_404(server_id)
    region_id = server.region_id

    db.session.delete(server)
    db.session.commit()

    return redirect(url_for('region.detail', region_id=region_id))
