from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db.models import DO_NOTHING


class User(AbstractUser):
    fullname = models.CharField(max_length=100)
    role = models.ForeignKey(to='Role', on_delete=DO_NOTHING, null=True, blank=True)


class Role(models.Model):
    roli = models.CharField(max_length=100)

    def __str__(self):
        return self.roli


class Notification(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    def __str__(self):
        return self.message