from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Employees, Jobs, Countries

def get_employees(request):
    # employees = Employees.objects.filter(first_name="Steven")
    # employees = Employees.objects.filter(last_name="Chen")
    employees = Employees.objects.all()
    employees_list = ""
    for employee in employees:
        employees_list += f"<li>{employee.first_name} {employee.last_name}</li>"
    return HttpResponse(employees_list)

def get_jobs(request):
    # jobs = Jobs.objects.filter(job_id=1)
    # jobs = Jobs.objects.filter(min_salary=2500.0)
    jobs = Jobs.objects.filter(max_salary=30000.0)
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