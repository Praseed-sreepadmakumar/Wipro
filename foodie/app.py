from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# --------------------
# In-memory Databases
# --------------------
restaurants = {}
dishes = {}
users = {}
orders = {}
ratings = {}

# --------------------
# Helpers
# --------------------
def generate_id():
    return str(uuid4())

def not_found(message="Resource not found"):
    return jsonify({"error": message}), 404


# =====================================================
# 1. Restaurant Module
# =====================================================

@app.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400

    for r in restaurants.values():
        if r["name"] == data["name"]:
            return jsonify({"error": "Restaurant already exists"}), 409

    restaurant_id = generate_id()
    restaurant = {
        "id": restaurant_id,
        "name": data["name"],
        "category": data.get("category"),
        "location": data.get("location"),
        "images": data.get("images"),
        "contact": data.get("contact"),
        "enabled": True,
        "approved": False
    }
    restaurants[restaurant_id] = restaurant
    return jsonify(restaurant), 201


@app.route("/api/v1/restaurants/<restaurant_id>", methods=["PUT"])
def update_restaurant(restaurant_id):
    if restaurant_id not in restaurants:
        return not_found("Restaurant not found")

    restaurants[restaurant_id].update(request.json)
    return jsonify(restaurants[restaurant_id]), 200


@app.route("/api/v1/restaurants/<restaurant_id>/disable", methods=["PUT"])
def disable_restaurant(restaurant_id):
    if restaurant_id not in restaurants:
        return not_found("Restaurant not found")

    restaurants[restaurant_id]["enabled"] = False
    return jsonify({"message": "Restaurant disabled"}), 200


@app.route("/api/v1/restaurants/<restaurant_id>", methods=["GET"])
def view_restaurant(restaurant_id):
    if restaurant_id not in restaurants:
        return not_found("Restaurant not found")

    return jsonify(restaurants[restaurant_id]), 200


# =====================================================
# 2. Dish Module
# =====================================================

@app.route("/api/v1/restaurants/<restaurant_id>/dishes", methods=["POST"])
def add_dish(restaurant_id):
    if restaurant_id not in restaurants:
        return not_found("Restaurant not found")

    data = request.json
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid dish data"}), 400

    dish_id = generate_id()
    dish = {
        "id": dish_id,
        "restaurant_id": restaurant_id,
        "name": data["name"],
        "type": data.get("type"),
        "price": data["price"],
        "available_time": data.get("available_time"),
        "image": data.get("image"),
        "enabled": True
    }
    dishes[dish_id] = dish
    return jsonify(dish), 201


@app.route("/api/v1/dishes/<dish_id>", methods=["PUT"])
def update_dish(dish_id):
    if dish_id not in dishes:
        return not_found("Dish not found")

    dishes[dish_id].update(request.json)
    return jsonify(dishes[dish_id]), 200


@app.route("/api/v1/dishes/<dish_id>/status", methods=["PUT"])
def dish_status(dish_id):
    if dish_id not in dishes:
        return not_found("Dish not found")

    dishes[dish_id]["enabled"] = request.json.get("enabled", True)
    return jsonify({"message": "Dish status updated"}), 200


@app.route("/api/v1/dishes/<dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    if dish_id not in dishes:
        return not_found("Dish not found")

    del dishes[dish_id]
    return jsonify({"message": "Dish deleted"}), 200


# =====================================================
# 3. Admin Module
# =====================================================

@app.route("/api/v1/admin/restaurants/<restaurant_id>/approve", methods=["PUT"])
def approve_restaurant(restaurant_id):
    if restaurant_id not in restaurants:
        return not_found("Restaurant not found")

    restaurants[restaurant_id]["approved"] = True
    return jsonify({"message": "Restaurant approved"}), 200


@app.route("/api/v1/admin/restaurants/<restaurant_id>/disable", methods=["PUT"])
def admin_disable_restaurant(restaurant_id):
    if restaurant_id not in restaurants:
        return not_found("Restaurant not found")

    restaurants[restaurant_id]["enabled"] = False
    return jsonify({"message": "Restaurant disabled by admin"}), 200


@app.route("/api/v1/admin/feedback", methods=["GET"])
def view_feedback():
    return jsonify(list(ratings.values())), 200


@app.route("/api/v1/admin/orders", methods=["GET"])
def view_all_orders():
    return jsonify(list(orders.values())), 200


# =====================================================
# 4. User Module
# =====================================================

@app.route("/api/v1/users/register", methods=["POST"])
def register_user():
    data = request.json
    if not data or "email" not in data:
        return jsonify({"error": "Invalid user data"}), 400

    for u in users.values():
        if u["email"] == data["email"]:
            return jsonify({"error": "User already exists"}), 409

    user_id = generate_id()
    user = {
        "id": user_id,
        "name": data.get("name"),
        "email": data["email"],
        "password": data.get("password")
    }
    users[user_id] = user
    return jsonify(user), 201


@app.route("/api/v1/restaurants/search", methods=["GET"])
def search_restaurants():
    name = request.args.get("name", "").lower()
    location = request.args.get("location", "").lower()

    result = [
        r for r in restaurants.values()
        if name in r["name"].lower()
        and location in (r["location"] or "").lower()
    ]
    return jsonify(result), 200


# =====================================================
# 5. Order & Rating Module
# =====================================================

@app.route("/api/v1/orders", methods=["POST"])
def place_order():
    data = request.json
    if not data or "user_id" not in data or "restaurant_id" not in data:
        return jsonify({"error": "Invalid order data"}), 400

    order_id = generate_id()
    order = {
        "id": order_id,
        "user_id": data["user_id"],
        "restaurant_id": data["restaurant_id"],
        "dishes": data.get("dishes", []),
        "status": "PLACED"
    }
    orders[order_id] = order
    return jsonify(order), 201


@app.route("/api/v1/ratings", methods=["POST"])
def give_rating():
    data = request.json
    if not data or "order_id" not in data:
        return jsonify({"error": "Invalid rating data"}), 400

    rating_id = generate_id()
    rating = {
        "id": rating_id,
        "order_id": data["order_id"],
        "rating": data.get("rating"),
        "comment": data.get("comment")
    }
    ratings[rating_id] = rating
    return jsonify(rating), 201


@app.route("/api/v1/restaurants/<restaurant_id>/orders", methods=["GET"])
def orders_by_restaurant(restaurant_id):
    result = [o for o in orders.values() if o["restaurant_id"] == restaurant_id]
    return jsonify(result), 200


@app.route("/api/v1/users/<user_id>/orders", methods=["GET"])
def orders_by_user(user_id):
    result = [o for o in orders.values() if o["user_id"] == user_id]
    return jsonify(result), 200


# =====================================================
# Run App
# =====================================================
if __name__ == "__main__":
    app.run(debug=True)
