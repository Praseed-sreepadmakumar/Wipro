from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

patients = []

@app.route("/")
def home():
    return render_template("register.html")

# -------------------------
# GET all patients
# -------------------------
@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(patients), 200


# -------------------------
# Register a patient
# -------------------------
@app.route("/api/patients", methods=["POST"])
def add_patient():
    data = request.get_json()

    required_fields = ["name", "age", "gender", "contact", "disease", "doctor"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Invalid patient data"}), 400

    patients.append(data)
    return jsonify({"message": "Patient registered"}), 201


# -------------------------
# Get patient by name
# -------------------------
@app.route("/api/patients/<name>", methods=["GET"])
def get_patient(name):
    for patient in patients:
        if patient["name"] == name:
            return jsonify(patient), 200
    return jsonify({"error": "Patient not found"}), 404


# -------------------------
# Update patient info
# -------------------------
@app.route("/api/patients/<name>", methods=["PUT"])
def update_patient(name):
    data = request.get_json()
    for patient in patients:
        if patient["name"] == name:
            patient.update(data)
            return jsonify({"message": "Patient updated"}), 200
    return jsonify({"error": "Patient not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
