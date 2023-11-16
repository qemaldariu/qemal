from rest_framework import serializers
from .models import EmployeeInformation


class SerializeEmployee(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInformation
        exclude = ('is_deleted', )
