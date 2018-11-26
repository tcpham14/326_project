from .models import Student
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(label=("Username"), max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label=("Username"), max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
 

# class StudentForm(forms.ModelForm):

# 	class Meta:
# 		model = Student
# 		fields = ['user']
# 		# fields = ['user', 'major', 'concentration', 'fav_courses', 'current_courses', 'bio', 'grad_year', 'num_classes_taken', 'num_liked_reviews']
# 		# widgets = {
# 		# 	'major': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Major', 'style': 'margin-top: 7px'}),
# 		# 	'concentration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concentration', 'style': 'margin-top:7px'}), 
# 		# }
