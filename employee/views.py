from django.contrib.auth.models import User
from employee.serializers import SerializeEmployee
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser


class SoftDeleteModelMixin:
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()




class EmployeeModifyRetrieveDelete(SoftDeleteModelMixin, RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = SerializeEmployee
    permission_classes = [IsAdminUser]
