from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Min, Max, Count
from rest_framework.views import APIView
from employees.serializers import CountrySalaryMetrics

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # @action(detail=True, methods=['get'])
    # def salary(self, request, pk=None):
    #     employee = self.get_object()
    #     gross = employee.salary

    #     if employee.country == "India":
    #         tds = gross * 0.10
    #     elif employee.country == "United States":
    #         tds = gross * 0.12
    #     else:
    #         tds = 0

    #     return Response({
    #         "gross_salary": gross,
    #         "tds": tds,
    #         "net_salary": gross - tds
    #     })

    # @action(detail=False, methods=['get'])
    # def high_salary(self, request):
    #     employees = Employee.objects.filter(salary__gt=100000)
    #     serializer = self.get_serializer(employees, many=True)
    #     return Response(serializer.data)

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