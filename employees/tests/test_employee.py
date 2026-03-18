import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_employee():
    client = APIClient()

    data = {
        "full_name": "Shakiv Ali",
        "job_title": "Backend Developer",
        "country": "India",
        "salary": 50000
    }

    response = client.post("/employees/", data,format="json")

    assert response.status_code == 201
    assert response.data["full_name"] == "Shakiv Ali"