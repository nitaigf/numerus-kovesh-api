def test_healthcheck(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root_without_params_returns_landing_page(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "http://localhost:5173" in response.text
    assert "/?doc=openapi" in response.text
    assert "/?doc=redoc" in response.text


def test_root_redirects_to_redoc_when_doc_param_is_redoc(client):
    response = client.get("/?doc=redoc", follow_redirects=False)

    assert response.status_code in (302, 307)
    assert response.headers["location"] == "/redoc"