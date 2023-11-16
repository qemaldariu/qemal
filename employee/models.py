from django.db import models
from django.db.models import DO_NOTHING
from hr_manager.models import Department

from users.models import User

EMPLOYEE_STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Done', 'Done'),
    ('Canceled', 'Canceled'),
)


class EmployeeInformation(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    position = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='Pending')
    department = models.ForeignKey(to=Department, on_delete=DO_NOTHING)
    profilepicture = models.ImageField(upload_to='employee_profile_pics/', default='default.jpg', null=True,
                                       blank=True)
    is_deleted = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=DO_NOTHING, null=True)
    status = models.CharField(max_length=20, choices=EMPLOYEE_STATUS_CHOICES, default='Pending')


    def __str__(self):
        return f"{self.name} {self.surname}"
    #
    # EMPLOYEE_STATUS_CHOICES = (
    #     ('Pending', 'Pending'),
    #     ('Done', 'Done'),
    #     ('Canceled', 'Canceled'),
    # )

class LeaveAndAttendance(models.Model):

    employee = models.ForeignKey(to=EmployeeInformation, on_delete=DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=EMPLOYEE_STATUS_CHOICES, default='Pending')
    is_deleted = models.BooleanField(default=False)


class EmployeePerformance(models.Model):
    employee = models.ForeignKey(to=EmployeeInformation, on_delete=DO_NOTHING)
    performance = models.TextField(default=None)
    status = models.CharField(max_length=20, choices=EMPLOYEE_STATUS_CHOICES, default='Pending')
    is_deleted = models.BooleanField(default=False)



class EmployeeTraining(models.Model):
    employee = models.ForeignKey(to=EmployeeInformation, on_delete=DO_NOTHING)
    status = models.CharField(max_length=20, choices=EMPLOYEE_STATUS_CHOICES, default='Pending')
    is_deleted = models.BooleanField(default=False)



class Report(models.Model):
    employee = models.ForeignKey(to=EmployeeInformation, on_delete=DO_NOTHING)
    reports = models.TextField(max_length=100, default=None)
    status = models.CharField(max_length=20, choices=EMPLOYEE_STATUS_CHOICES, default='Pending')
    is_deleted = models.BooleanField(default=False)

