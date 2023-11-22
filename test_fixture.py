from fastapi.testclient import TestClient
from main import app
import pytest  # imports everything from pytest


@pytest.fixture
def client():  # every time a client fixture is referenced it will create a new test client
    yield TestClient(
        app
    )  # yield is a generator and is equivalent to return, with some differences.


# use GET/DELETE API, PUT API; needs to get used first - code repetition
# 1) Fixture = precondition to test case, Pre-istallation of an object and return it
# 2) Providing a matrix of inputs and receiving a matrix of outputs
# 3) Mock - blackbox testing


@pytest.fixture
def good_payload():
    return {
        "name": "first item",
        "quantity": 5,
        "serial_num": "324",
        "origin": {"country": "Ethiopia", "production_date": "2023"},
    }


@pytest.fixture
def bad_payload():
    return {
        "name": "first item",
        "quantity": "five",
        "serial_num": "324",
        "origin": {"country": "Ethiopia", "production_date": "2023"},
    }


@pytest.fixture
def create_and_delete_item(good_payload):
    client.put("/items/test", json=good_payload)
    yield "Item Created"
    client.delte(f"/items/test/{good_payload.serial_num}")


def test_put_incorrect_imput_api(bad_payload, client):
    response = client.put("/items/test", json=bad_payload)
    assert response.status_code == 422


def test_get_api(client, good_payload):
    response = client.get("/items/test")
    assert response.status_code == 404


def test_put_then_get_api(client, good_payload):
    response = client.put("/items/test/", json=good_payload)
    assert response.status_code == 200
    response = client.get(f"/items/test/")
    assert response.status_code == 200 and response.json() == good_payload


# parametrize allows to put thru many test cases at once, include parameter names as strings
# first test case a = 1, b = 2, expected = 3
# second test case a = 5, b = -1, expected = 4
@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 3), (5, -1, 4), (3, 3, 6)],
)
def test_addition(a, b, expected):
    assert a + b == expected


# @pytest.fixture
@pytest.mark.parametrize(
    "payload, http_code",
    [
        (  # Test Case 1
            {
                "name": "first item",
                "quantity": 5,
                "serial_num": "test",
                "origin": {"country": "Ethiopia", "production_date": "2023"},
            },
            200,
        ),
        (  # Test Case 2
            {
                "name": "first item",
                "quantity": "A",  # the incorrect input
                "serial_num": "test",
                "origin": {"country": "Ethiopia", "production_date": "2023"},
            },
            422,
        ),
    ],
    # indirect=[
    #     "payload"
    # ],  # indirectly saying we're evaluating the good payload and bad payload
)
def test_many_put_apis(client, payload, http_code):
    # Check if the response's status_code equal to the expected http_code
    assert client.put("/items/test/", json=payload).status_code == http_code


@pytest.mark.parametrize(
    "item_serial_num, payload, expected_http_code",
    [
        (  # Test Case 1
            "111",  # item_serial_num
            {  # payload
                "name": "first item",
                "quantity": 5,
                "serial_num": "111",
                "origin": {"country": "Ethiopia", "production_date": "2023"},
            },
            200,  # expected http_code
        ),
        (  # Test Case 2
            "222",  # item_serial_num
            None,  # payload
            404,  # expected http_code
        ),
    ],
)
def test_many_get_apis(client, item_serial_num, payload, expected_http_code):
    # If the payload is None, we will not call the PUT API to add item to the database
    # Because we want to test the 404 test case
    if payload is not None:
        client.put(f"/items/{item_serial_num}/", json=payload)

    # Check if the response's status_code equal to the expected http_code
    response = client.get(f"/items/{item_serial_num}/")
    assert response.status_code == expected_http_code

    # Check if the response's payload equal to the one that we using to call PUT API to create the item
    if payload is not None:
        assert response.json() == payload
