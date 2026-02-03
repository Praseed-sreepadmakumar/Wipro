import requests
import pytest

@pytest.mark.parametrize("patient", [
    {
        "name": "Alice",
        "age": 30,
        "gender": "Female",
        "contact": "9999999999",
        "disease": "Fever",
        "doctor": "Dr. Smith"
    },
    {
        "name": "Bob",
        "age": 45,
        "gender": "Male",
        "contact": "8888888888",
        "disease": "Diabetes",
        "doctor": "Dr. John"
    }
])
def test_register_patient(base_url, patient):
    response = requests.post(f"{base_url}/api/patients", json=patient)
    assert response.status_code == 201


def test_get_all_patients(base_url):
    response = requests.get(f"{base_url}/api/patients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.xfail
def test_get_invalid_patient(base_url):
    response = requests.get(f"{base_url}/api/patients/Unknown")
    assert response.status_code == 200
