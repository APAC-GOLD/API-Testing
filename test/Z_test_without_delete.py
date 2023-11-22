#My Unit Test

from fastapi.testclient import TestClient
from main import app

#look for files with test_*.py
# $ pytest 
# command: pytest -vvl

# Unit Tests
def test_basic_example():
    #pass 
    assert(True)

client = TestClient(app)

def test_put_api():
    response = client.put("/items/420", json={
        "name": "first item",
        "quantity": 5,
        "serial_num": "324",
        "origin": {
            "country": "Ethiopia",
            "production_date": "2023"
        }
    })
    assert response.status_code == 200


# Tests API when we put in incorrect input; The API will return the message that the input is incorrect, and which field is incrorrect. 
def test_put_incorrect_imput_api():
    response = client.put("/items/422", json={
        "name": "first item",
        "quantity": "incorrect input", #quantity should be an integer i.e 5
        "serial_num": "324",
        "origin": {
            "country": "Ethiopia",
            "production_date": "2023"
        }
    })
    assert response.status_code == 422

# then run "pytest -vvl" again to test GET API 
def test_get_api():
    response = client.put("/items/420", json={
        "name": "first item",
        "quantity": 501,
        "serial_num": "324",
        "origin": {
            "country": "Ethiopia",
            "production_date": "2023"
        }
    })
    
    assert response.status_code == 200
    response = client.get("/items/420",)
    assert response.status_code == 200
    assert response.json() == {
        "name": "first item",
        "quantity": 501,
        "serial_num": "324",
        "origin": {
            "country": "Ethiopia",
            "production_date": "2023"
        }
    }