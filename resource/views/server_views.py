from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.utils import redirect
from resource import db
from resource.models import Region, Server, Usage

from resource.forms import ServerCreateForm

bp = Blueprint('server', __name__, url_prefix='/server')


@bp.route('/<int:region_id>/')
def list(region_id):
    form = ServerCreateForm()
    regions = Region.query.all()
    region = Region.query.get_or_404(region_id)
    servers = Server.query.filter_by(region_id=region_id)

    if form.validate_on_submit():
        host = request.form.get('Host')
        cpu = request.form.get('CPU')
        memory = request.form.get('Memory')
        instance = request.form.get('Instance')
        server = Server(region_id=region.id, host=host,
                        cpu=cpu, memory=memory, instance=instance)
        region.servers.append(server)
        db.session.commit()
        return redirect(url_for('region.detail'), region_id=region_id)

    return render_template('region/region_detail.html', regions=regions, region=region, servers=servers, form=form)
