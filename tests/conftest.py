import pytest
from resource import create_app
from resource.models import User, Region, Server, Usage


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope='module')
def new_user():
    # given
    data = {
        'name': 'test_user',
        'email': 'test@test.com',
        'password': 123456
    }

    # when
    user = User(data['name'], data['email'], data['password'])

    return user


@pytest.fixture(scope='module')
def new_region():
    # given
    data = {
        'name': 'test_region'
    }

    # when
    region = Region(data['name'])

    return region


@pytest.fixture(scope='module')
def new_server():
    # given
    data = {
        'region_id': 1,
        'host': 'test_host',
        'cpu': 10,
        'memory': 100,
        'storage': 1000
    }

    # when
    server = Server(
        data['region_id'],
        data['host'],
        data['cpu'],
        data['memory'],
        data['storage']
    )

    return server


@pytest.fixture(scope='module')
def new_usage():
    # given
    data = {
        'server_id': 1,
        'cpu_usage': 5,
        'memory_usage': 50,
        'storage_usage': 500,
        'note': 'test_note',
        'record_date': '2022-08-01'
    }

    # when
    usage = Usage(
        data['server_id'],
        data['cpu_usage'],
        data['memory_usage'],
        data['storage_usage'],
        data['note'],
        data['record_date']
    )

    return usage
