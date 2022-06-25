from resource import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'User {self.name}'

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'Region {self.name}'


class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region_id = db.Column(db.Integer(), db.ForeignKey(
        'region.id'))
    region = db.relationship('Region', backref=db.backref(
        'servers', cascade='all, delete-orphan'))
    host = db.Column(db.String(100), nullable=False, unique=True)
    cpu = db.Column(db.Integer(), nullable=False)
    memory = db.Column(db.Integer(), nullable=False)
    storage = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Server {self.host}'


class Usage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer(), db.ForeignKey(
        'server.id'))
    server = db.relationship('Server', backref=db.backref(
        'logs', cascade='all, delete-orphan'))
    cpu_usage = db.Column(db.Integer(), nullable=False)
    memory_usage = db.Column(db.Integer(), nullable=False)
    storage_usage = db.Column(db.Integer(), nullable=False)
    note = db.Column(db.Text(), nullable=True)
    record_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f'Usage {self.server} in {self.record_date}'

# use date format to save record date
# ex) date(2022, 6, 1)
# user datetime format when searching
# ex) Usage.query.filter_by(record_date=datetime.datetime(2022, 6, 1, 0, 0)).first()
