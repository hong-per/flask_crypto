local_url = "http://127.0.0.1:5000"


def test_create_server_page(client):
    response = client.get(f"{local_url}/server/create/region1/")
    assert response.status_code == 200


def test_update_server_page(client):
    response = client.get(f"{local_url}/server/update/1/")
    assert response.status_code == 200

# TODO: test CRUD functions