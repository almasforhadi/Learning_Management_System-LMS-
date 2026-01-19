from django.urls import path
from .views import AdminOnlyView, RegisterView, ProfileView, ForgetPasswordView, ResetPasswordView  

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('forget-password/', ForgetPasswordView.as_view()),
    path('reset-password/', ResetPasswordView.as_view()),
    path('admin-test/', AdminOnlyView.as_view()),
]