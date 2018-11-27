from .models import Student, Class
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name', 'style': 'margin-top: 7px'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'style': 'margin-top: 7px'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com', 'style': 'margin-top: 7px'}))
    password1 = forms.Field(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'style': 'margin-top: 7px'}))
    password2 = forms.Field(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'style': 'margin-top: 7px'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'style': 'margin-top: 7px'}),        }

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(label=("Username"), max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label=("Username"), max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class EditUserForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        """If no initial data, provide some defaults."""
        initial = kwargs.get('initial', {})
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        initial['email'] = user.email
        kwargs['initial'] = initial
        super(EditUserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']




class EditStudentForm(forms.ModelForm):
    # def __init__(self, exp=None, *args, **kwargs):
    #     super(EditStudentForm, self).__init__(*args, **kwargs)
    #     if exp:
    #         self.fields['bio'].initial = exp
    def __init__(self, user, *args, **kwargs):
        """If no initial data, provide some defaults."""
        initial = kwargs.get('initial', {})
        initial['bio'] = user.student.bio
        # initial['major'] = 
        initial['concentration'] = user.student.concentration
        # initial['fav_courses'] = user.student.fav_courses
        # initial['current_courses'] = user.student.current_courses
        initial['grad_year'] = user.student.grad_year
        kwargs['initial'] = initial
        super(EditStudentForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Student
        fields = ['bio', 'major', 'concentration', 'fav_courses', 'current_courses', 'grad_year']











# class StudentForm(forms.ModelForm):

# 	class Meta:
# 		model = Student
# 		fields = ['user']
# 		# fields = ['user', 'major', 'concentration', 'fav_courses', 'current_courses', 'bio', 'grad_year', 'num_classes_taken', 'num_liked_reviews']
# 		# widgets = {
# 		# 	'major': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Major', 'style': 'margin-top: 7px'}),
# 		# 	'concentration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concentration', 'style': 'margin-top:7px'}), 
# 		# }
