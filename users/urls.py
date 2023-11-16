from django.urls import path
from users.views import UserRegistrationView, UserLoginView, NotificationList

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    path('api/notifications/', NotificationList.as_view(), name='notification-list')
]

