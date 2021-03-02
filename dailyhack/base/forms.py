from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.contrib.auth.models import User

#create the user model form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']