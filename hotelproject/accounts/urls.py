from django.urls import path
from .views import login_email, verify_email_otp

urlpatterns = [
    path('email-login/', login_email, name='email_login'),
    path('verify-email/', verify_email_otp, name='verify_email'),
]
