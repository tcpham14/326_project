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
    random_index_list = random.sample(range(len(class_list)), 4)
    class_featured = class_list[random_index_list[0]]
    class_featured_1 = class_list[random_index_list[1]]
    class_featured_2 = class_list[random_index_list[2]]
    class_featured_3 = class_list[random_index_list[3]]
    feedback_1 = random.choice(Feedback.objects.filter(course = class_featured_1))
    feedback_2 = random.choice(Feedback.objects.filter(course = class_featured_2))
    feedback_3 = random.choice(Feedback.objects.filter(course = class_featured_3))
    highest_rated_class_list = Class.objects.all()
    
    feedback_list = {}
    user_list = {}
    for i in range(0, len(highest_rated_class_list) - 1):
        feedback_list[i] = random.choice(Feedback.objects.filter(course=highest_rated_class_list[i]))
        user_list[i] = feedback_list[i].user
    # feedback_count = {}
    # for course in class_list:
    #     feedback_count[course.class_id] = Class.objects.filter(feedback__courses=course).count()

    sorted_classes = []
    class_list = Class.objects.all()
    for course in class_list:
       sorted_classes.append((course, 0))
       for course_feedback in Feedback.objects.filter(course=course.class_id):
           sorted_classes[len(sorted_classes)-1] = (sorted_classes[len(sorted_classes)-1][0], sorted_classes[len(sorted_classes)-1][1] + int(course_feedback.rating))
       sorted_classes[len(sorted_classes)-1] = (sorted_classes[len(sorted_classes)-1][0], sorted_classes[len(sorted_classes)-1][1] / len(Feedback.objects.filter(course=course.class_id)))

    sorted_classes.sort(key=lambda x: x[1])
    sorted_classes.reverse()

    highest_rated_class_list = [i[0] for i in sorted_classes]

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
        "feedback_1": feedback_1,
        "feedback_2": feedback_2,
        "feedback_3": feedback_3
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
        context['user_feedback'] = Feedback.objects.filter(user=pk).all()
        context['feedback_count'] = Feedback.objects.filter(user=pk).count()
        context['favorite_courses'] = Class.objects.filter(user=pk).all()
        return context