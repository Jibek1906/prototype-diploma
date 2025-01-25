from django import forms
from django.contrib.auth.models import User
from .models import UserDetails

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['height', 'weight', 'goal', 'training_level']  # All required fields for user details

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
