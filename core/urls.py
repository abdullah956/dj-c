from django.urls import path
from .views import trigger_email

urlpatterns = [
    path('send/', trigger_email),
]
