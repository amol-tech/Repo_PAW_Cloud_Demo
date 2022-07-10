from django import forms
from app_emp_reg.models import Employee
import proj_host_paw.settings as settings

class DateInput(forms.DateInput):
    input_type = 'date'

class EmloyeeForm(forms.ModelForm):
    DESIG_CHOICES = (('Manager','Manager'),
                     ('Officer', 'Officer'),
                     ('Clerk', 'Clerk'),
                     ('Engineer', 'Engineer'),
                     ('Worker', 'Worker'),
                     ('Salesman', 'Salesman')
    )

    joining_date = forms.DateField(localize=True,widget=DateInput)
    designation = forms.ChoiceField(choices=DESIG_CHOICES)

    class Meta():
        model = Employee
        fields = '__all__'

