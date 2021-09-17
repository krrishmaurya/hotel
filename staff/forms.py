from django import forms
from django.forms.widgets import PasswordInput


class Login_form(forms.Form):
    user_name=forms.CharField(max_length=10)
    password=forms.CharField(widget=PasswordInput())
    