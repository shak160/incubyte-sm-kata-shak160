from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.full_name
