from django.shortcuts import render
from app_emp_reg.models import Department,Employee

# Create your views here.
def index_main(request):
    return render(request, 'app_emp_reg/main.html')

def index_employee(request):
    list_emp = Employee.objects.order_by('name')
    dict_emp = {'emp_records': list_emp}
    return render(request, 'app_emp_reg/employee.html', context=dict_emp)

def index_raw_emp(request):
    list_emp = Employee.objects.order_by('name')
    dict_emp = {'emp_records': list_emp}
    return render(request, 'app_emp_reg/raw_emp.html', context=dict_emp)

def index_department(request):
    list_dept = Department.objects.order_by('name')
    dict_dept = {'dept_records': list_dept}
    return render(request, 'app_emp_reg/department.html', context=dict_dept)