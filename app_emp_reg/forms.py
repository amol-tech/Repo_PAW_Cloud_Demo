from django import forms
from app_emp_reg.models import Employee
import proj_host_paw.settings as settings

class DateInput(forms.DateInput):
    input_type = 'date'

class EmloyeeForm(forms.ModelForm):
    joining_date = forms.DateField(localize=True,widget=DateInput)

    class Meta():
        model = Employee
        fields = '__all__'

