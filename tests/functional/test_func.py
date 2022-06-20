from resource import create_app
from tests.conftest import client
from flask import session
import json
import config

local_url = "http://127.0.0.1:5000"


def test_request_example(client):
    response = client.get(f"{local_url}/auth/login/")
    # assert b"<h5>Login</h5>" in response.data
    assert response.status_code == 200


def test_access_session(client):
    with client:
        client.post(f"{local_url}/auth/login", data={
            "name": "test",
            "password": 123456
        })

    response = client.get(f"{local_url}/")
    assert response.status_code == 200
