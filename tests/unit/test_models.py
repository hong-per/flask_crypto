def test_new_user_with_fixture(new_user):

    assert new_user.name == 'test_user'
    assert new_user.email == 'test@test.com'
    assert new_user.password == 123456

def test_new_region_with_fixture(new_region):

    assert new_region.name == 'test_region'


def test_new_server_with_fixture(new_server):

    assert new_server.region_id == 1
    assert new_server.host == 'test_host'
    assert new_server.cpu == 10
    assert new_server.memory == 100
    assert new_server.storage == 1000


def test_new_usage_with_fixture(new_usage):

    assert new_usage.server_id == 1
    assert new_usage.cpu_usage == 5
    assert new_usage.memory_usage == 50
    assert new_usage.storage_usage == 500
    assert new_usage.note == 'test_note'
    assert new_usage.record_date == '2022-08-01'