from django.urls import path,re_path
from app_emp_reg import views

app_name = 'app_emp_reg'

urlpatterns = [
    path('sigma/', views.index_main, name='index_main'),
    path('employees/', views.index_employee, name='index_employee'),
    path('departments/', views.index_department, name='index_department'),
]