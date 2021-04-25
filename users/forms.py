from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
	# email = forms.EmailField()
	# first_name = forms.CharField(max_length=30)
	# last_name = forms.CharField(max_length=30)
	
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')

		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError(("This email address is already in use. Please supply a different email address."))
		return email

	def update_details(self):
		password = self.cleaned_data.get('password1')
		firstname = self.cleaned_data.get('first_name')
		lastname = self.cleaned_data.get('last_name') 

class EditProf(UserChangeForm):

	class Meta:
		model = User
		fields = {'first_name', 'last_name', 'email'}

class ExtendedUserForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ('p_image',)