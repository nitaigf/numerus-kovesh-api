def test_numerology_route_returns_expected_payload(client):
    response = client.post("/v1/numerology", json={"text": "Nitai Garcia Fernandes"})

    assert response.status_code == 200
    assert response.json() == {
        "input": "Nitai Garcia Fernandes",
        "normalized": "NITAIGARCIAFERNANDES",
        "letters": [
            {"char": "N", "value": 5},
            {"char": "I", "value": 9},
            {"char": "T", "value": 2},
            {"char": "A", "value": 1},
            {"char": "I", "value": 9},
            {"char": "G", "value": 7},
            {"char": "A", "value": 1},
            {"char": "R", "value": 9},
            {"char": "C", "value": 3},
            {"char": "I", "value": 9},
            {"char": "A", "value": 1},
            {"char": "F", "value": 6},
            {"char": "E", "value": 5},
            {"char": "R", "value": 9},
            {"char": "N", "value": 5},
            {"char": "A", "value": 1},
            {"char": "N", "value": 5},
            {"char": "D", "value": 4},
            {"char": "E", "value": 5},
            {"char": "S", "value": 1},
        ],
        "sum": 85,
        "reduced": 4,
        "is_master": False,
        "meaning": "Estrutura",
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