import pytest
from resource import create_app
from resource.models import User


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
