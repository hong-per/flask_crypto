from resource import db
from resource.models import Server, Usage
from datetime import datetime
from flask_seeder import Seeder
import random
from faker import Faker


class UsageSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):

        fake = Faker()

        # Create usages for each server from 1st Jan to 1st June
        for server in range(1, 41):
            for month in range(1, 6):
                seed_usage = Usage(
                    server_id=server,
                    cpu_usage=random.randint(1, 12),
                    memory_usage=random.randint(1, 64),
                    storage_usage=random.randint(1, 1000),
                    note=fake.sentence(),
                    record_date=datetime(2022, month, 1, 0, 0)
                )
                db.session.add(seed_usage)
