from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), #HOMEPAGE
    path("", views.cs326, name="cs326") ##DONT KNOW WHAT THIS IS FOR
    
]
