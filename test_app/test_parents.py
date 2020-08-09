from fastapi.testclient import TestClient
import json, jsonpath
import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from app import app

test_parent_id = None

with open(os.path.join(os.path.dirname(__file__), "test_parent_json.json"), "r") as f:
    json_input = f.read()
request_json = json.loads(json_input)

client = TestClient(app)


def test_create_parent():
    response = client.post(
        "/parents/",
        json=request_json
    )
    assert response.status_code == 200


def test_create_existing_parent():
    response = client.post(
        "/parents/",
        json=request_json
    )
    assert response.status_code == 400


def test_get_parents():
    global test_parent_id
    response = client.get(
        "/parents/"
    )
    response_json = json.loads(response.text)[-1]
    test_parent_id = jsonpath.jsonpath(response_json, 'id')[0]
    assert response.status_code == 200


def test_get_parent():
    response = client.get(
        "/parents/{}".format(test_parent_id)
    )
    assert response.status_code == 200


def test_get_non_existing_parent():
    response = client.get(
        "/parents/{}".format(int(test_parent_id) + 1)
    )
    assert response.status_code == 404


def test_get_non_existing_parent():
    response = client.get(
        "/parents/{}".format(int(test_parent_id) + 1)
    )
    assert response.status_code == 404


def test_update_parent():
    response = client.put(
        "/parents/{}".format(test_parent_id),
        json=request_json
    )
    assert response.status_code == 200


def test_delete_parent():
    response = client.delete(
        "/parents/{}".format(test_parent_id)
    )
    assert response.status_code == 200


def test_delete_non_existing_parent():
    response = client.delete(
        "/parents/{}".format(test_parent_id)
    )
    assert response.status_code == 404
