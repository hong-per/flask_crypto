local_url = "http://127.0.0.1:5000"


def test_dashboard_page(client):
    response = client.get(f"{local_url}/")
    assert response.status_code == 200
