from resource import db
from resource.models import Server
from flask_seeder import Seeder, Faker, generator


class ServerSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create Server objects
        faker = Faker(
            cls=Server,
            init={
                "region_id": generator.Integer(start=1, end=8),
                "host": generator.Name(),
                "cpu": generator.Integer(start=4, end=12),
                "memory": generator.Integer(start=16, end=64),
                "storage": generator.Integer(start=500, end=1000)
            }
        )

        # Create 5 servers
        for server in faker.create(5):
            print("Adding server: %s" % server)
            self.db.session.add(server)
