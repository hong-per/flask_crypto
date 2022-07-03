from resource import db
from resource.models import Server
from flask_seeder import Seeder


class ServerSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        regions = ['east', 'west', 'south', 'north']

        # Create 10 servers for each region
        for region in regions:
            for server_num in range(1, 11):
                seed_server = Server(
                    region_id=(regions.index(region) + 1),
                    host=f"{region}{server_num}",
                    cpu=12,
                    memory=64,
                    storage=1000
                )
                db.session.add(seed_server)
