from django.shortcuts import render
from spew.models import Book, Author, BookInstance


# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


def class_page(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
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
