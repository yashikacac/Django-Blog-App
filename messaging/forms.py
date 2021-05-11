from django import forms
from .models import Message




class msg_form(forms.ModelForm):
	
	class Meta:
		model = Message
		fields = ('text','receiver',)