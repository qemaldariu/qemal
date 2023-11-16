from rest_framework import BasePermission



class IsHR(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.roli == 'HR'


    def has_object_permission(self, request, view, obj):

        return True


class IsEmployee(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user  # nqs useri i loguar esht njelloj me userin e sistemit shto fushen user kudo te kesh prb me ownership
