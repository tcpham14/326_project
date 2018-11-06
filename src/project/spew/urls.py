from django.urls import path
from . import views

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
]
