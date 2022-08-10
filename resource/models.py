from resource import db
from functools import reduce


class User(db.Model):
    __tablename__ = 'user'

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
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'Region {self.name}'

    def __init__(self, name: str):
        self.name = name

    # For Dashboard graph
    def recent_logs(self):
        logs = sum([server.logs for server in self.servers], [])
        recent_date = max(log.record_date for log in logs)
        return list(filter(lambda x: x.record_date == recent_date, logs))

    def cpu_usage(self):
        return reduce(lambda x, y: x + y, [log.cpu_usage for log in self.recent_logs()])

    def total_cpu(self):
        return reduce(lambda x, y: x + y, [server.cpu for server in self.servers])

    def memory_usage(self):
        return reduce(lambda x, y: x + y, [log.memory_usage for log in self.recent_logs()])

    def total_memory(self):
        return reduce(lambda x, y: x + y, [server.memory for server in self.servers])

    def storage_usage(self):
        return reduce(lambda x, y: x + y, [log.storage_usage for log in self.recent_logs()])

    def total_storage(self):
        return reduce(lambda x, y: x + y, [server.storage for server in self.servers])

    # For Trend graph
    def logs(self):
        return sum([server.logs for server in self.servers], [])

    def dates(self):
        return sorted(list(set([log.record_date for log in self.logs()])))

    def cpu_usage_by_date(self):
        cpu_usages = []
        for date in self.dates():
            date_logs = list(
                filter(lambda x: x.record_date == date, self.logs()))
            cpu_usages.append(
                reduce(lambda x, y: x + y, [log.cpu_usage for log in date_logs]))

        return cpu_usages

    def memory_usage_by_date(self):
        memory_usages = []
        for date in self.dates():
            date_logs = list(
                filter(lambda x: x.record_date == date, self.logs()))
            memory_usages.append(
                reduce(lambda x, y: x + y, [log.memory_usage for log in date_logs]))

        return memory_usages

    def storage_usage_by_date(self):
        storage_usages = []
        for date in self.dates():
            date_logs = list(
                filter(lambda x: x.record_date == date, self.logs()))
            storage_usages.append(
                reduce(lambda x, y: x + y, [log.storage_usage for log in date_logs]))

        return storage_usages


class Server(db.Model):
    __tablename__ = 'server'

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

    def __init__(self, region_id: int, host: str, cpu: int, memory: int, storage: int):
        self.region_id = region_id
        self.host = host
        self.cpu = cpu
        self.memory = memory
        self.storage = storage


class Usage(db.Model):
    __tablename__ = 'usage'

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

    def __init__(self, server_id: int, cpu_usage: int, memory_usage: int, storage_usage: int, note: str, record_date: str):
        self.server_id = server_id
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.storage_usage = storage_usage
        self.note = note
        self.record_date = record_date

# use date format to save record date
# ex) date(2022, 6, 1)
# user datetime format when searching
# ex) Usage.query.filter_by(record_date=datetime.datetime(2022, 6, 1, 0, 0)).first()
