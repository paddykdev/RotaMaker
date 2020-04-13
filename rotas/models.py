from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_am = models.BooleanField(blank=False, default=True)
    is_pm = models.BooleanField(blank=False, default=True)
    is_evening = models.BooleanField(blank=False, default=True)
    shifts_week = models.IntegerField(blank=False, default=5)
    shifts_assigned = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"