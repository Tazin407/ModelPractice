from django import forms
from .models import Employee

class EmpData(forms.ModelForm):
    class Meta:
        model= Employee
        exclude= ['id']
        labels= {
            'name': 'Employee Name',
            'age': 'Employee Age',
        }