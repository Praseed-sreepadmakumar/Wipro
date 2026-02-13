import pytest
import requests

BASE_URL = "http://localhost:5000/api/v1"

# -------------------------
# Fixtures
# -------------------------

@pytest.fixture(scope="module")
def restaurant():
    payload = {
        "name": "Test Food Hub",
        "category": "Indian",
        "location": "Bangalore"
    }
    response = requests.post(f"{BASE_URL}/restaurants", json=payload)
    assert response.status_code == 201
    return response.json()


@pytest.fixture(scope="module")
def approved_restaurant(restaurant):
    r_id = restaurant["id"]
    response = requests.put(f"{BASE_URL}/admin/restaurants/{r_id}/approve")
    assert response.status_code == 200
    return restaurant


@pytest.fixture(scope="module")
def dish(approved_restaurant):
    r_id = approved_restaurant["id"]
    payload = {
        "name": "Paneer Butter Masala",
        "type": "Veg",
        "price": 250
    }
    response = requests.post(f"{BASE_URL}/restaurants/{r_id}/dishes", json=payload)
    assert response.status_code == 201
    return response.json()


@pytest.fixture(scope="module")
def user():
    payload = {
        "name": "John",
        "email": "john@test.com",
        "password": "1234"
    }
    response = requests.post(f"{BASE_URL}/users/register", json=payload)
    assert response.status_code == 201
    return response.json()


@pytest.fixture(scope="module")
def order(user, approved_restaurant, dish):
    payload = {
        "user_id": user["id"],
        "restaurant_id": approved_restaurant["id"],
        "dishes": [dish["id"]]
    }
    response = requests.post(f"{BASE_URL}/orders", json=payload)
    assert response.status_code == 201
    return response.json()


# -------------------------
# Test Cases
# -------------------------

def test_register_restaurant():
    payload = {"name": "Another Restaurant"}
    response = requests.post(f"{BASE_URL}/restaurants", json=payload)
    assert response.status_code == 201


def test_search_restaurant(restaurant):
    response = requests.get(f"{BASE_URL}/restaurants/search?name=Test")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_place_order(order):
    assert order["status"] == "PLACED"


def test_give_rating(order):
    payload = {
        "order_id": order["id"],
        "rating": 5,
        "comment": "Excellent!"
    }
    response = requests.post(f"{BASE_URL}/ratings", json=payload)
    assert response.status_code == 201
    assert response.json()["rating"] == 5


def test_view_orders_by_user(user):
    response = requests.get(f"{BASE_URL}/users/{user['id']}/orders")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_view_orders_by_restaurant(restaurant):
    response = requests.get(f"{BASE_URL}/restaurants/{restaurant['id']}/orders")
    assert response.status_code == 200
