from django.contrib import admin

from spew.models import Author, Genre, Book, BookInstance

admin.site.register(Genre)


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # By setting the list_display variable in an Admin class will have
    # it display only the fields in the model that are specified.
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")

    # By setting the fields variable in an Admin class will only
    # display the specified fields in the "detail view" of the
    # model. Fields are displayed vertically by default, but will
    # display horizontally if you further group them in a tuple as we
    # do here for the birth and death dates.
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]

    inlines = [BookInline]


# Sometimes, it is useful to display associated information of a
# related model in the detail view. In this case, we define a tabular
# inline class that will allow us to display BookInstance data in the
# same Book detail view. See where it is used in the BookAdmin class.


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # By setting the list_display variable in an Admin class will have
    # it display only the fields in the model that are
    # specified. Notice that we do not specify the genre field for
    # this Admin class because it is a many-to-many field. This can be
    # a costly operation when accessing the database. So, we have it
    # display the results of a function call (display_genre) - see the
    # defintion of this function in the Book class in models.py.
    list_display = ("title", "author", "display_genre")

    # This allows us to display information about the corresponding
    # book instances of this book. It is clearly useful to be able to
    # see which book instances we have for a book. Because the
    # BookInstance model defines a "foreign key" on Book, Django will
    # automatically be able to look up the associated book instances.
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "due_back")

    # By setting the list_filter variable in an Admin class it will be
    # used to populate a "filter" UI box component in the admin site
    # to allow the user to only display particular items.
    list_filter = ("status", "due_back")

    # You can add "sections" to group related model information within
    # the detail forum using the "fieldsets" attribute. This is done
    # by creating a tuple of section tuples. The first value of each
    # tuple is the title of the section (None, if no title), followed
    # by a dictionary containing the entry "fields" that correspond to
    # the fields the section will have.
    fieldsets = (
        (None, {"fields": ("book", "imprint", "id")}),
        ("Availability", {"fields": ("status", "due_back")}),
    )
