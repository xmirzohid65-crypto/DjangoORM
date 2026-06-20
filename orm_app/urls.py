from django.urls import path
from .views import get_employees, get_jobs, get_countries

urlpatterns = [
    path('get_employees/', get_employees),
    path('get_jobs/', get_jobs),
    path('get_countries/', get_countries)
]