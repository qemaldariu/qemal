from django.db import models
from django.db.models import DO_NOTHING

from users.models import User

RECRUIT_STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Done', 'Done'),
    ('Canceled', 'Canceled'),
)


class Department(models.Model):
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=RECRUIT_STATUS_CHOICES, default='Pending')
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.department


class HrManager(models.Model):
    name = models.CharField(max_length=100, default=None)
    surname = models.CharField(max_length=100, default=None)
    status = models.CharField(max_length=20, default='Pending')
    birthday = models.DateField()
    birthplace = models.CharField(max_length=50)
    profilepicture = models.ImageField(upload_to='hrmanager_profile_pics/', default='default.jpg', null=True,
                                       blank=True)
    user = models.ForeignKey(to=User, on_delete=DO_NOTHING, null=True)
    status = models.CharField(max_length=20, choices=RECRUIT_STATUS_CHOICES, default='Pending')
    is_deleted = models.BooleanField(default=False)




from django.db import models
from django.db.models import DO_NOTHING
from hr_manager.models import Department




class Recruit(models.Model):
    name = models.CharField(max_length=100, default="Default Name")
    surname = models.CharField(max_length=100, default=None)
    user = models.ForeignKey(to=User, on_delete=DO_NOTHING, null=True)

    application_deadline = models.DateField()
    status = models.CharField(max_length=20, default='Pending')
    birthday = models.DateField()
    birthplace = models.CharField(max_length=50)
    department = models.ForeignKey(to=Department, on_delete=DO_NOTHING, default=None)
    profilepicture = models.ImageField(upload_to='recruits_profile_pics/', default='default.jpg', null=True,
                                       blank=True)
    status = models.CharField(max_length=20, choices=RECRUIT_STATUS_CHOICES, default='Pending')
    is_deleted = models.BooleanField(default=False)




class RecruitPerformance(models.Model):
    name = models.ForeignKey(to=Recruit, on_delete=DO_NOTHING)
    performance = models.TextField(default=None)
    status = models.CharField(max_length=20, choices=RECRUIT_STATUS_CHOICES, default='Pending')
    is_deleted = models.BooleanField(default=False)


class RecruitTraining(models.Model):
    name = models.ForeignKey(to=Recruit, on_delete=DO_NOTHING)
    status = models.CharField(max_length=20, default='Pending')
    training = models.TextField(max_length=100, default=None)
    status = models.CharField(max_length=20, choices=RECRUIT_STATUS_CHOICES, default='Pending')
    is_deleted = models.BooleanField(default=False)


class Report(models.Model):
    employee = models.ForeignKey(to=Recruit, on_delete=DO_NOTHING)
    reports = models.TextField(max_length=100, default=None)
    status = models.CharField(max_length=20, choices=RECRUIT_STATUS_CHOICES, default='Pending')
    is_deleted = models.BooleanField(default=False)



class LeaveAndAttendance(models.Model):
    employee = models.ForeignKey(to=Recruit, on_delete=DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=RECRUIT_STATUS_CHOICES, default='Pending')
    is_deleted = models.BooleanField(default=False)

