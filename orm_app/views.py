# Create your views here.
from django.http import HttpResponse
from .models import *

def get_employees(request):
    employees = Employees.objects.filter(first_name="Steven")
    # employees = Employees.objects.filter(last_name="Chen")
    # employees = Employees.objects.all()
    employees_list = ""
    for employee in employees:
        employees_list += f"<li>{employee.first_name} {employee.last_name}</li>"
    return HttpResponse(employees_list)

def get_jobs(request):
    # jobs = Jobs.objects.filter(job_id=1)
    jobs = Jobs.objects.filter(min_salary=2500.0)
    # jobs = Jobs.objects.filter(max_salary=30000.0)
    jobs_list = ""
    for job in jobs:
        jobs_list += f"<li>{job.job_title}</li>"
    return HttpResponse(jobs_list)

def get_countries(request):
    # countries = Countries.objects.filter(country_name="United Kingdom")
    # countries = Countries.objects.filter(country_id="EG")
    countries = Countries.objects.filter(
        country_id="US",
        country_name="United States of America"
    )
    countries_list = ""
    for country in countries:
        countries_list += f"""* {country.country_name}"""
    return HttpResponse(countries_list)

def get_regions(request):
    # regions = Regions.objects.filter(region_id = 4)
    regions = Regions.objects.filter(region_name = "Americas")
    regions_list = ""
    for region in regions:
        regions_list += f"<li>{region.region_name}</li>"
    return HttpResponse(regions_list)

def get_locations(request):
    # locatinos = Locations.objects.filter(city = "New York")
    # locations = Locations.objects.filter(street_address = "Magdalen Centre, The Oxford Science Park")
    locations = Locations.objects.filter(
        postal_code=98199,
        state_province="Washington"
    )
    locations_list = ""
    for location in locations:
        locations_list += f"<li>{location.country}</li>"
    return HttpResponse(locations_list)

def get_departments(request):
    departments = Departments.objects.filter(department_id=10)
    # departments = Departments.objects.filter(department_name="IT")
    departments = Departments.objects.filter(
        department_id=11,
        department_name="Accounting"
    )
    departments_list = ""
    for department in departments:
        departments_list += f"<li>{department.department_name}</li>"
    return HttpResponse(departments_list)

def get_dependents(request):
    # dependents = Dependents.objects.filter(first_name="Sandra")
    # dependents = Dependents.objects.filter(relationship = "Child")
    dependents = Dependents.objects.filter(
        last_name="Khoo",
        relationship="Child",
        employee=115
    )
    dependents_list = ""
    for dependent in dependents:
        dependents_list += f"<li>{dependent.first_name} {dependent.last_name}</li>"
    return HttpResponse(dependents_list)