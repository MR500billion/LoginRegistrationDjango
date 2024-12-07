from django import forms 
from django.contrib.auth.models import User


class SignUp(forms.ModelForm):
	first_name = forms.CharField(min_length=2, max_length=50)
	last_name = forms.CharField(min_length=2, max_length=50)
	email = forms.CharField(
		min_length=6,max_length=70,widget=forms.EmailInput())
	username = forms.CharField(min_length=4,max_length=50)
	password = forms.CharField(max_length=70,widget=forms.PasswordInput())
	password_confirmation = forms.CharField(max_length=70,widget=forms.PasswordInput())

	

	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','password']

	def clean_password2(self):
		password = self.cleaned_data.get('password')
		password_confirmation = self.cleaned_data.get('password_confirmation')
		if password and password_confirmation and password != password_confirmation:
			raise forms.ValidationError("Passwords don't match")
		return password_confirmation


