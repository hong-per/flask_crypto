from resource import db
from resource.models import Region
from flask_seeder import Seeder, Faker, generator


class RegionSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create Region objects
        faker = Faker(
            cls=Region,
            init={
                "name": generator.Name()
            }
        )

        # Create 5 regions
        for region in faker.create(5):
            print("Adding region: %s" % region)
            self.db.session.add(region)
