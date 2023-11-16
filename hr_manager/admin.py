from django.contrib import admin
from .models import HrManager, Department

# Register your models here.
admin.site.register(HrManager)
admin.site.register(Department)
from .models import Recruit, RecruitPerformance, RecruitTraining, Report, LeaveAndAttendance

# Register your models here.
admin.site.register(Recruit)
admin.site.register(RecruitPerformance)
admin.site.register(RecruitTraining)
admin.site.register(Report)
admin.site.register(LeaveAndAttendance)
