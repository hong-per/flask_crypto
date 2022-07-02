from resource import db
from resource.models import Usage
from datetime import datetime
from flask_seeder import Seeder, Faker, generator


class UsageSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create Usage objects
        faker = Faker(
            cls=Usage,
            init={
                "server_id": generator.Integer(start=1, end=8),
                "cpu_usage": generator.Integer(start=4, end=12),
                "memory_usage": generator.Integer(start=16, end=64),
                "storage_usage": generator.Integer(start=500, end=1000),
                "note": generator.Name(),
                "record_date": datetime(2022, 1, 1, 0, 0)

            }
        )

        # Create 5 usages
        for usage in faker.create(5):
            print("Adding usage: %s" % usage)
            self.db.session.add(usage)
