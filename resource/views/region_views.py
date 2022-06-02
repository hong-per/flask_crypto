from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.utils import redirect
from resource import db
from resource.models import Region, Server, Usage
from resource.forms import ServerCreateForm

bp = Blueprint('region', __name__, url_prefix='/region')


@bp.route('/<int:region_id>/', methods=('GET', 'POST'))
def detail(region_id):
    form = ServerCreateForm()
    regions = Region.query.all()
    region = Region.query.get_or_404(region_id)
    servers = Server.query.filter_by(region_id=region_id)

    if request.method == 'POST' and form.validate_on_submit():
        server = Server(region_id=region_id, host=form.host.data, cpu=form.cpu.data,
                        memory=form.memory.data, instance=form.instance.data)
        db.session.add(server)
        db.session.commit()

    return render_template('region/region_detail.html', regions=regions, region=region, servers=servers, form=form)
