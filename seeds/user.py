from resource import db
from flask_seeder import Seeder, Faker, generator

# SQLAlchemy database model


class User(db.Model):
    def __init__(self, id=None, name=None, email=None, password=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return "ID=%d, Name=%s, Email=%s, Password=%s" % (self.id, self.name, self.email, self.password)

# All seeders inherit from Seeder


class UserSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=User,
            init={
                "id": generator.Sequence(start=4),
                "name": generator.Name(),
                "email": generator.Name(),
                "password": generator.Name()
            }
        )

        # Create 5 users
        for user in faker.create(5):
            print("Adding user: %s" % user)
            self.db.session.add(user)
