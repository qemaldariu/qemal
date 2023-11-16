from django.shortcuts import render
from employee.models import Employee
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from employee.serializers import SerializeEmployee
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from HR_management_project.employee.models import EmployeeInformation


class GetAllEmployee(APIView):
    def get(self, requests):
        employee = Employee.objects.all()
        our_serializer = SerializeEmployee(Employee, many=True)
        # our_serializer.is_valid()
        return Response(our_serializer.data)

    from django.shortcuts import render

    def custom_404(request, exception=None):
        return render(request, '404.html', status=404)

    class EmployeeListCreate(ListCreateAPIView):
        queryset = EmployeeInformation.objects.all()
        serializer_class = SerializeEmployee
        permission_classes = [AllowAny]

    class EmployeeModifyRetrieveDelete(RetrieveUpdateDestroyAPIView):
        queryset = EmployeeInformation.objects.all()
        serializer_class = SerializeEmployee
        permission_classes = [AllowAny]
