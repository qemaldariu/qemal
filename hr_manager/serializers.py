from rest_framework import serializers
from .models import HrManager, Department


class SerializeDepartment:
    class Meta:
        model = Department
        exclude = ('is_deleted', )


class SerializeHrManager:
    class Meta:
        model = HrManager
        exclude = ('is_deleted', )
