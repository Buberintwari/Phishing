# phishing_simulation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.phishing_page, name='phishing_page'),
]
