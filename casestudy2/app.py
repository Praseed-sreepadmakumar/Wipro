from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
movies = [
    {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    }
]

bookings = []

# -------------------------
# GET all movies
# -------------------------
@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200


# -------------------------
# GET movie by ID
# -------------------------
@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


# -------------------------
# ADD new movie
# -------------------------
@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.get_json()

    if not data or "id" not in data:
        return jsonify({"error": "Invalid data"}), 400

    movies.append(data)
    return jsonify({"message": "Movie added successfully"}), 201


# -------------------------
# UPDATE movie
# -------------------------
@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.get_json()

    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(data)
            return jsonify({"message": "Movie updated"}), 200

    return jsonify({"error": "Movie not found"}), 404


# -------------------------
# DELETE movie
# -------------------------
@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted"}), 200

    return jsonify({"error": "Movie not found"}), 404


# -------------------------
# BOOK tickets
# -------------------------
@app.route("/api/bookings", methods=["POST"])
def book_tickets():
    data = request.get_json()

    required_fields = ["movie_id", "tickets"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Invalid booking data"}), 400

    for movie in movies:
        if movie["id"] == data["movie_id"]:
            total_price = movie["price"] * data["tickets"]
            booking = {
                "movie": movie["movie_name"],
                "tickets": data["tickets"],
                "total_price": total_price
            }
            bookings.append(booking)
            return jsonify(booking), 201

    return jsonify({"error": "Movie not found"}), 404


if __name__ == "__main__":
    app.run(port=5000,debug=True)
