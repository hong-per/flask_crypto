local_url = "http://127.0.0.1:5000"


def test_region_page(client):
    response = client.get(f"{local_url}/region/1/")
    assert response.status_code == 200


def test_trend_page(client):
    response = client.get(f"{local_url}/trend/1/")
    assert response.status_code == 200