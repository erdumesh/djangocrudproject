from django.core import validators
from django import forms
from . models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['First_Name', 'Last_Name', 'Phone_Number','Email_ID','Address']
        widgets = {
            'First_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Last_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Phone_Number' : forms.NumberInput(attrs={'class':'form-control'}),
            'Email_ID' : forms.EmailInput(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class':'form-control'}),
        }