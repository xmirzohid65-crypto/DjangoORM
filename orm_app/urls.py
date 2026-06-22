from django.urls import path
from .views import *

urlpatterns = [
    path('get-employees/', get_employees),
    path('get-jobs/', get_jobs),
    path('get-countries/', get_countries),
    path('get-regions/', get_regions),
    path('get-locations/', get_locations),
    path('get-departments/', get_departments),
    path('get-dependents/', get_dependents),
]