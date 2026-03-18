import pytest
from rest_framework.test import APIClient
from employees.models import Employee
from employees.serializers import CountrySalaryMetrics

@pytest.mark.django_db
def test_salary_metrics_by_country():
    # Create sample employees
    Employee.objects.create(full_name="John Doe", job_title="Engineer", country="India", salary=100000)
    Employee.objects.create(full_name="Jane Smith", job_title="Manager", country="India", salary=150000)
    Employee.objects.create(full_name="Bob Lee", job_title="Analyst", country="USA", salary=120000)

    client = APIClient()
    response = client.get("/metrics/")

    assert response.status_code == 200

    # Validate response structure
    data = response.data
    assert isinstance(data, list)
    assert any(item["country"] == "India" for item in data)
    assert any(item["country"] == "USA" for item in data)
