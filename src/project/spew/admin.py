from django.contrib import admin

from spew.models import Class, User, Professor, Feedback, Subject

#admin.site.register(Genre)


#class ClassInline(admin.TabularInline):
#    model = Class
class UserInline(admin.TabularInline):
    model = User

class ClassInline(admin.TabularInline):
    model = Class

class FeedbackInline(admin.TabularInline):
    model = Feedback

class ProfessorInline(admin.TabularInline):
    model = Professor

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    # By setting the list_display variable in an Admin class will have
    # it display only the fields in the model that are specified.
    list_display = ["subject_name"]

    # By setting the fields variable in an Admin class will only
    # display the specified fields in the "detail view" of the
    # model. Fields are displayed vertically by default, but will
    # display horizontally if you further group them in a tuple as we
    # do here for the birth and death dates.
    
    inlines = [ClassInline]


# Sometimes, it is useful to display associated information of a
# related model in the detail view. In this case, we define a tabular
# inline class that will allow us to display BookInstance data in the
# same Book detail view. See where it is used in the BookAdmin class.


#class ProfessorInline(admin.TabularInline):
#    model = Professor


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # By setting the list_display variable in an Admin class will have
    # it display only the fields in the model that are specified.
    list_display = ("first_name", "last_name", "major", "concentration")

    # By setting the fields variable in an Admin class will only
    # display the specified fields in the "detail view" of the
    # model. Fields are displayed vertically by default, but will
    # display horizontally if you further group them in a tuple as we
    # do here for the birth and death dates.
    fields = ["first_name", "last_name", "major"]
    list_filter = ("major", "concentration")
    inlines = [FeedbackInline]


# Sometimes, it is useful to display associated information of a
# related model in the detail view. In this case, we define a tabular
# inline class that will allow us to display BookInstance data in the
# same Book detail view. See where it is used in the BookAdmin class.


#class ProfessorInline(admin.TabularInline):
#    model = Professor


class MembershipInline(admin.TabularInline):
    model = Professor.course.through

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    # By setting the list_display variable in an Admin class will have
    # it display only the fields in the model that are
    # specified. Notice that we do not specify the genre field for
    # this Admin class because it is a many-to-many field. This can be
    # a costly operation when accessing the database. So, we have it
    # display the results of a function call (display_genre) - see the
    # defintion of this function in the Book class in models.py.
    list_display = ("title", "class_id", "subject", "code", "attendance", "exams") #need to add the professor
    fields = ["title"]
    # This allows us to display information about the corresponding
    # book instances of this book. It is clearly useful to be able to
    # see which book instances we have for a book. Because the
    # BookInstance model defines a "foreign key" on Book, Django will
    # automatically be able to look up the associated book instances.
    # inlines = [ProfessorInline]
    inlines = [FeedbackInline, MembershipInline]



@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "contact")

    # By setting the list_filter variable in an Admin class it will be
    # used to populate a "filter" UI box component in the admin site
    # to allow the user to only display particular items.
    list_filter = ("first_name", "last_name")

    # You can add "sections" to group related model information within
    # the detail forum using the "fieldsets" attribute. This is done
    # by creating a tuple of section tuples. The first value of each
    # tuple is the title of the section (None, if no title), followed
    # by a dictionary containing the entry "fields" that correspond to
    # the fields the section will have.
    inlines = [MembershipInline]
    exclude = ('course',)
    
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("user","comment", "course", "professor",  "rating", "date", )
    list_filter = ("course", "user", "professor")
    # inlines = [UserInline]
    

