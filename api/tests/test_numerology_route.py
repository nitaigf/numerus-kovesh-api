def test_numerology_route_returns_expected_payload(client):
    response = client.post("/v1/numerology", json={"text": "Nitai Embrás"})

    assert response.status_code == 200
    assert response.json() == {
        "input": "Nitai Embrás",
        "normalized": "NITAIEMBRAS",
        "letters": [
            {"char": "N", "value": 5},
            {"char": "I", "value": 9},
            {"char": "T", "value": 2},
            {"char": "A", "value": 1},
            {"char": "I", "value": 9},
            {"char": "E", "value": 5},
            {"char": "M", "value": 4},
            {"char": "B", "value": 2},
            {"char": "R", "value": 9},
            {"char": "A", "value": 1},
            {"char": "S", "value": 1},
        ],
        "sum": 48,
        "reduced": 3,
        "is_master": False,
        "meaning": "Comunicacao",
    }


def test_numerology_route_returns_semantic_422_for_invalid_input(client):
    response = client.post("/v1/numerology", json={"text": "!!! 123"})

    assert response.status_code == 422
    assert response.json() == {
        "detail": {
            "code": "invalid_input_text",
            "message": "Input must contain at least one valid letter.",
        }
    }