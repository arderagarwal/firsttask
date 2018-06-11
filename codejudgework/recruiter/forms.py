from django import forms
from django.contrib.auth.models import User
from recruiter.models import Recruiter

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','first_name','last_name','password')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),

        }

class RecruiterForm(forms.ModelForm):
    class Meta():
        model = Recruiter
        fields = ('PhoneNo',)
        widgets = {
            'PhoneNo': forms.TextInput(attrs={'class':'form-control'}),
        }
