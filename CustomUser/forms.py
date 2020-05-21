from django import forms
from .models import Customuser


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customuser
        fields = ['username', 'first_name', 'last_name',
                  'Display_name', 'password', 'email', 'Age', ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
