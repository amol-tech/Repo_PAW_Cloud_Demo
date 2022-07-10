from django.contrib import admin
from app_emp_reg.models import Department,Employee,Customer,CustomerAccountDetail,CustomerAdmin

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(CustomerAccountDetail)