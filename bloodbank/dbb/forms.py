from django import forms
from .models import User

class UsersForm(forms.ModelForm):
	class Meta:
		model = signup
		fields = ['username','email','password','confirmpassword']