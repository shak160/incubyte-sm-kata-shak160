from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Min, Max, Count
from rest_framework.views import APIView
from employees.serializers import CountrySalaryMetrics

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing employee instances.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SalaryMetricsView(APIView):
    def get(self, request):
        metrics = (
            Employee.objects.values("country")
            .annotate(
                average_salary=Avg("salary"),
                employee_count=Count("id")
            )
        )
        serializer = CountrySalaryMetrics(metrics, many=True)
        return Response(serializer.data)