from django.db import models

# Create your models here.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomerUser
class SignUpForm(UserCreationForm):
    

    class Meta:
        model= CustomerUser
        fields = ('username', 'password1', 'password2', )