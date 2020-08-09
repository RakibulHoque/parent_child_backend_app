from fastapi.testclient import TestClient
import json, jsonpath
import os,sys,inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0,parent_dir)

from app import app

test_parent_id = None
test_child_id = None

with open(os.path.join(os.path.dirname(__file__),"test_parent_json.json"), "r") as f:
    json_input = f.read()
request_parent_json = json.loads(json_input)

with open(os.path.join(os.path.dirname(__file__),"test_child_json.json"), "r") as f:
    json_input = f.read()
request_child_json = json.loads(json_input)

client = TestClient(app)


def test_create_parent():
    response = client.post(
        "/parents/",
        json=request_parent_json
    )
    assert response.status_code == 200


def test_get_parents():
    global test_parent_id
    response = client.get(
        "/parents/"
    )
    response_json = json.loads(response.text)[-1]
    test_parent_id = jsonpath.jsonpath(response_json, 'id')[0]
    assert response.status_code == 200


def test_create_child():
    response = client.post(
        f"/parents/{test_parent_id}/children/",
        json=request_child_json
    )
    assert response.status_code == 200


def test_create_child():
    response = client.post(
        f"/parents/{test_parent_id}/children/",
        json=request_child_json
    )
    assert response.status_code == 200


def test_create_non_existing_parents_child():
    response = client.post(
        f"/parents/{int(test_parent_id)+1}/children/",
        json=request_child_json
    )
    assert response.status_code == 404


def test_get_children():
    global test_child_id
    response = client.get(
        "/children/"
    )
    response_json = json.loads(response.text)[-1]
    test_child_id = jsonpath.jsonpath(response_json, 'id')[0]
    assert response.status_code == 200


def test_get_child():
    response = client.get(
        "/children/{}".format(test_child_id)
    )
    assert response.status_code == 200


def test_get_non_existing_child():
    response = client.get(
        "/children/{}".format(int(test_child_id)+1)
    )
    assert response.status_code == 404


def test_update_child():
    response = client.put(
        "/children/{}".format(test_child_id),
        json=request_child_json
    )
    assert response.status_code == 200


def test_update_non_existing_child():
    response = client.put(
        "/children/{}".format(int(test_child_id)+1),
        json=request_child_json
    )
    assert response.status_code == 404


def test_delete_child():
    response = client.delete(
        "/children/{}".format(test_child_id)
    )
    assert response.status_code == 200


def test_delete_non_existing_child():
    response = client.delete(
        "/children/{}".format(test_child_id)
    )
    assert response.status_code == 404


def test_delete_parent():
    response = client.delete(
        "/parents/{}".format(test_parent_id)
    )
    assert response.status_code == 200
