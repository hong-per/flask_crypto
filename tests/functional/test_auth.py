local_url = "http://127.0.0.1:5000"


def test_request_example(client):
    response = client.get(f"{local_url}/auth/login/")
    assert response.status_code == 200


def test_access_session(client):
    with client:
        client.post(f"{local_url}/auth/login", data={
            "name": "test",
            "password": 123456
        })

    response = client.get(f"{local_url}/")
    assert response.status_code == 200
