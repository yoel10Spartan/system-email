from django.urls import path

from .views import send_email_user

urlpatterns = [
    path('email', send_email_user),
]