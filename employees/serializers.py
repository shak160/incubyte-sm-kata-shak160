from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class CountrySalaryMetrics(serializers.Serializer):
    country = serializers.CharField()
    average_salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    employee_count = serializers.IntegerField()
