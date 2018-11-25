from .models import User
from django import forms

class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'style': 'margin-top: 7px'}))

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'password']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'style': 'margin-top: 7px'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name ', 'style': 'margin-top:7px'}), 
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'style': 'margin-top:7px'}),
			'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a password', 'style': 'margin-top:7px'})
			}