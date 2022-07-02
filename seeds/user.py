from resource import db
from resource.models import User
from flask_seeder import Seeder, Faker, generator


class UserSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=User,
            init={
                "name": generator.Name(),
                "email": generator.Name(),
                "password": generator.Name()
            }
        )

        # Create 5 users
        for user in faker.create(5):
            print("Adding user: %s" % user)
            self.db.session.add(user)
