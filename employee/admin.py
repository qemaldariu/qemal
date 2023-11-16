from django.contrib import admin
from .models import EmployeeInformation, LeaveAndAttendance, EmployeePerformance, EmployeeTraining, Report

admin.site.register(EmployeeInformation)
admin.site.register(LeaveAndAttendance)
admin.site.register(EmployeePerformance)
admin.site.register(EmployeeTraining)
admin.site.register(Report)
