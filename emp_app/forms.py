from django import forms 
from django.db import models 
from django.forms import fields
from . models import Department,Role,Employee

class EmpForm(forms.ModelForm):
    class Meta :
        model=Employee 
        fields="__all__"