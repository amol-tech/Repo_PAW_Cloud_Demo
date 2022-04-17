from django.urls import path,re_path
from app_emp_reg import views

app_name = 'app_emp_reg'

urlpatterns = [
    path('sigma/', views.index_main, name='index_main'),
    path('employees/', views.EmployeeListView.as_view(), name='index_employees'),
    path('departments/', views.index_department, name='index_departments'),
    path('raw_emp/', views.index_raw_emp, name='index_raw_emp'),
    re_path(r'^employees/(?P<pk>\w+)/$', views.EmployeeUpdateView.as_view(), name='index_employee_update'),
]