from resource import db
from flask_seeder import Seeder, Faker, generator

# SQLAlchemy database model


class Region(db.Model):
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name


    def __str__(self):
        return "ID=%d, Name=%s" % (self.id, self.name)

# All seeders inherit from Seeder


class RegionSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=Region,
            init={
                "id": generator.Sequence(start=6),
                "name": generator.Name()
            }
        )

        # Create 5 regions
        for region in faker.create(5):
            print("Adding region: %s" % region)
            self.db.session.add(region)
