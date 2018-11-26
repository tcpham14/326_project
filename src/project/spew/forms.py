from .models import Student
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'style': 'margin-top: 7px'}))

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'password']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'style': 'margin-top: 7px'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'style': 'margin-top:7px'}), 
			'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email ', 'style': 'margin-top:7px'}), 
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'style': 'margin-top:7px'}),
			'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a password', 'style': 'margin-top:7px'})
			}

# class StudentForm(forms.ModelForm):

# 	class Meta:
# 		model = Student
# 		fields = ['user']
# 		# fields = ['user', 'major', 'concentration', 'fav_courses', 'current_courses', 'bio', 'grad_year', 'num_classes_taken', 'num_liked_reviews']
# 		# widgets = {
# 		# 	'major': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Major', 'style': 'margin-top: 7px'}),
# 		# 	'concentration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concentration', 'style': 'margin-top:7px'}), 
# 		# }
