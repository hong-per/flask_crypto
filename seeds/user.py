from resource import db
from resource.models import User
from flask_seeder import Seeder


class UserSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):

        # Create 5 users
        for user_num in range(1, 5):
            print("Adding user: %s" % user_num)
            seed_user = User(
                name=f"test{user_num}",
                email=f"test{user_num}@flask_resource.com",
                password="Test1234"
            )
            self.db.session.add(seed_user)
