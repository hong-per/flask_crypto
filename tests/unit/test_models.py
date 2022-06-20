from resource.models import User, Region
from tests.conftest import new_user


def test_new_user_with_fixture(new_user):
    
    assert new_user.name == 'test_user'
    assert new_user.email == 'test@test.com'
    assert new_user.password == 123456
