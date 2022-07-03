from resource import db
from resource.models import Region
from flask_seeder import Seeder


class RegionSeeder(Seeder):

    # run() will be called by Flask-Seeder
    def run(self):
        regions = ['east', 'west', 'south', 'north']

        # Create 4 regions
        for region in regions:
            print("Adding region: %s" % region)
            seed_region = Region(name=region)
            db.session.add(seed_region)
