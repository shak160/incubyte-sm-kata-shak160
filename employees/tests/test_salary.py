import pytest
from rest_framework.test import APIClient
from employees.models import Employee

@pytest.mark.django_db
def test_salary_calculation_india():
    client = APIClient()

    employee = Employee.objects.create(
        full_name="Shakiv Ali",
        job_title="Backend Developer",
        country="India",
        salary=100000
    )

    response = client.get(f"/employees/{employee.id}/salary/")

    assert response.status_code == 200
    assert response.data["gross_salary"] == 100000
    assert response.data["tds"] == 10000
    assert response.data["net_salary"] == 90000