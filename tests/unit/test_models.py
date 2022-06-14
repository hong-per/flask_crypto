from resource.models import User, Region


def test_new_user():
    # given
    data = {
        'name': 'test_user',
        'email': 'test@test.com',
        'password': 123456
    }

    # when
    user = User(data['name'], data['email'], data['password'])

    # then
    assert user.name == 'test_user'
    assert user.email == 'test@test.com'
    assert user.password == 123456


# def test_new_region():
#     # given
#     data = {
#         'name': 'test_region'
#     }

#     # when
#     region = Region(data['name'])

#     # then
#     assert region.name == 'test_region'
