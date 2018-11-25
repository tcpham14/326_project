from .models import SpewUser
from django import forms

class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = SpewUser
		fields = ['first_name', 'last_name', 'email', 'password']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'style': 'margin-top: 7px'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name ', 'style': 'margin-top:7px'}), 
			'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com', 'style': 'margin-top:7px'}),
			'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a password', 'style': 'margin-top:7px'})
			}