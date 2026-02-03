import requests

BASE_URL = "http://127.0.0.1:5000"


def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_movie():
    new_movie = {
        "id": 103,
        "movie_name": "Dune",
        "language": "English",
        "duration": "2h 35m",
        "price": 300
    }

    response = requests.post(f"{BASE_URL}/api/movies", json=new_movie)
    assert response.status_code == 201
    assert response.json()["message"] == "Movie added successfully"


def test_book_tickets():
    booking_data = {
        "movie_id": 101,
        "tickets": 2
    }

    response = requests.post(f"{BASE_URL}/api/bookings", json=booking_data)
    assert response.status_code == 201
    assert response.json()["tickets"] == 2
