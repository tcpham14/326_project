from django.shortcuts import render
from spew.models import User, Class, Professor, Feedback, Subject
from django.views import generic
import random
from django.views import generic

# Create your views here.
def index(request):
    '''"""View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()'''
    num_classes = Class.objects.all().count()
    popular_class_list = Class.objects.all()
    class_list = Class.objects.all()
    class_featured = random.choice(popular_class_list)
    class_featured_1 = random.choice(popular_class_list)
    class_featured_2 = random.choice(popular_class_list)
    class_featured_3 = random.choice(popular_class_list)

    feedback_list = Feedback.objects.all()
    user_list = User.objects.all()
    highest_rated_class_list = Class.objects.all()
    # feedback_count = {}
    # for course in class_list:
    #     feedback_count[course.class_id] = Class.objects.filter(feedback__courses=course).count()
    context = {
        "num_classes": num_classes,
        "class_featured": class_featured,
        "class_featured_1": class_featured_1,
        "class_featured_2": class_featured_2,
        "class_featured_3": class_featured_3,
        "popular_class_list": popular_class_list,
        "feedback_list": feedback_list,
        "user_list": user_list,
        "class_list": class_list,
        "highest_rated_class_list": highest_rated_class_list,
        # "class_list_popular": class_list_popular
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


def class_page(request):


    context = {

    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, "class_page.html", context=context) ##THIS IS HWERE HTE PAGE GOES

def profile(request):

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "profile.html", context=context) ##THIS IS HWERE HTE PAGE GOES

def search_results(request):

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "search_results.html", context=context) ##THIS IS HWERE HTE PAGE GOES

def submissions_page(request):

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "submissions_page.html", context=context) ##THIS IS HWERE HTE PAGE GOES
def advanced_search(request):

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "advanced_search.html", context=context) ##THIS IS HWERE HTE PAGE GOES


class ClassListView(generic.ListView):
    model = Class
    template_name = "class_list.html"


class ClassDetailView(generic.DetailView):
    model = Class
    template_name = "class_page.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        context = super(ClassDetailView, self).get_context_data(**kwargs)
        context['class_feedback'] = Feedback.objects.filter(course=pk)
        return context


class SearchResults(generic.ListView):
   model = Class
   template_name = "search_results.html"

class UserListView(generic.ListView):
    model = User
    template_name = "user_list.html"

class UserDetailView(generic.DetailView):
    model = User
    template_name = "profile.html"
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['user_feedback'] = Feedback.objects.filter(user=pk)
        return context