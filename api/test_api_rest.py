"""Script API: prueba de lectura (GET) y creación (POST) sobre JSONPlaceholder."""
import pytest
import requests
from jsonschema import validate
from api.schemas import POST_SCHEMA

pytestmark = pytest.mark.api
BASE = "https://jsonplaceholder.typicode.com"
TIMEOUT = 15


def test_api_posts():
    http = requests.Session()
    http.headers.update({"User-Agent": "taller-qa/1.0", "Accept": "application/json"})

    # Paso 1: GET /posts/1 -> 200, JSON, estructura y datos esperados
    r = http.get(f"{BASE}/posts/1", timeout=TIMEOUT)
    assert r.status_code == 200
    assert "application/json" in r.headers["Content-Type"]
    body = r.json()
    validate(instance=body, schema=POST_SCHEMA)
    assert body["id"] == 1 and body["userId"] == 1

    # Paso 2: POST /posts -> 201, estructura y eco de los campos enviados
    payload = {"title": "Taller QA", "body": "Automatización de pruebas", "userId": 7}
    r = http.post(f"{BASE}/posts", json=payload, timeout=TIMEOUT)
    assert r.status_code == 201
    body = r.json()
    validate(instance=body, schema=POST_SCHEMA)
    assert body["id"] == 101
    assert {k: body[k] for k in payload} == payload
