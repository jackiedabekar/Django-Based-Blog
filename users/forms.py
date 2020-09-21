#By default UserCreationForm dosent provide email functionality
#so we are using django builtin forms to add emailfield
from django import forms
#in blog we are dealing with User thats why imported user model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile 
"""
here we have created new form, by inherting functionality
of username and password from UserCreationForm and emailfield
from forms
"""
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class UserProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['image']