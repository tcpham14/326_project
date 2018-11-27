from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from . import forms

urlpatterns = [
    path("", views.index, name="index"), #HOMEPAGE
    path("users/", views.UserListView.as_view(), name="users"),
    path("classes/", views.ClassListView.as_view(), name="classes"),
    path("professors/", views.ProfessorListView.as_view(), name="professors"),

    path("class/<int:pk>", views.ClassDetailView.as_view(), name="class-detail"),
    path("user/<str:pk>", views.UserDetailView.as_view(), name="user-detail"),
    path("professor/<int:pk>", views.ProfessorDetailView.as_view(), name="professor-detail"),

    path("search_results", views.SearchResults, name="search_results"),
    path("submissions", views.submissions_page, name="submissions_page"),
    path("advanced_search", views.advanced_search, name="advanced_search"),
    path("accounts/register/", views.Registration, name="register"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=forms.LoginForm)),
    
    path("submissions/create/", views.FeedbackCreate.as_view(), name='feedback_create'),
]

'''
urlpatterns = [
    path("", views.index, name="index"), #HOMEPAGE
    path("users/", views.UserListView.as_view(), name="users"),
    path("classes/", views.ClassListView.as_view(), name="classes"),
    path("professors/", views.ProfessorListView.as_view(), name="professors"),

    path("class/<int:pk>", views.ClassDetailView.as_view(), name="class-detail"),
    path("user/<int:pk>", views.UserDetailView.as_view(), name="user-detail"),
    path("professor/<int:pk>", views.ProfessorDetailView.as_view(), name="professor-detail"),

    path("search_results", views.SearchResults, name="search_results"),
    path("submissions", views.submissions_page, name="submissions_page"),
    path("advanced_search", views.advanced_search, name="advanced_search"),
    path("accounts/register/", views.Registration, name="register"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=forms.LoginForm)),
      #{'template_name': 'spew/registration/login.html', 'authentication_form': forms.LoginForm},
      #name='login'),
]
'''

