from resource.models import User


def test_new_user():
    user = User('test', 'test@test.com', 123456)

    assert user.email == 'test@test.com'
    assert user.password == 123456
