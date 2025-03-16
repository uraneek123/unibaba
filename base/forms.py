from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl', 
    }))
     
     password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl', 
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        def clean_email(self):
            original_email = self.cleaned_data.get('email')
            email = original_email.split('@')[1] 
            if not email == "@ad.unsw.edu.au":
                raise forms.ValidationError({"Only @ad.unsw.edu.au email addresses allowed"})
            return email
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl', 
    }))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your First Name',
        'class': 'w-full py-4 px-6 rounded-xl', 
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Last Name',
        'class': 'w-full py-4 px-6 rounded-xl', 
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl', 
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl', 
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl', 
    }))