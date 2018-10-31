import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker

from spew.models import Professor, Book, BookInstance, Subject, Class

fake = Faker()

# Create Genres
subjects = [
    Subject(name="ENGLISH"),
    Subject(name="MATH"),
    Subject(name="COMPSCI"),
]

# Save the genres to the database
for subject in subjects:
    subject.save()

# Create Authors
professors = []
for i in range(1, 10):
    p_fname = fake.first_name()
    p_lname = fake.last_name()
    p_contact = fake.phone_number()
    professor = Professor(
        first_name=p_fname, last_name=p_lname, position="professor", contact=p_contact
    )
    professor.save()
    professors.append(professor)


# Create Books
classes = []
for i in range(1, 10):
    c_title = fake.text(50)
    c_professor = professors[fake.random_int(0, len(professors)) - 1]
    c_description = fake.text(1000)
    c_exams = fake.boolean(chance_of_getting_true=50)
    c_attendance = fake.boolean(chance_of_getting_true=50)
    c_textbooks = fake.text(1000)
    course = Class(title=c_title, professor=c_professor, description=c_description, exams=c_exams, attendance = c_attendance, textbooks = c_textbooks)
    classes.save()
    classes.subject.add(subjects[fake.random_int(0, len(genres)) - 1])
    classes.save()
    classes.append(course)

users = []
for i in range(1,10):
    u_fname = fake.firstname()
    u_lname = fake.lastname()
    u_major = subjects[fake.random_int(0, len(subjects)) - 1]
    user = User(first_name = u_fname, last_name = u_lastname, major = u_major)
    users.save()
    users.append(author)
    

print("Subject:")
for g in Subject.objects.all():
    print(g)

print("\nProfessor:")
for a in Professor.objects.all():
    print(a)

print("\nClass:")
for b in Class.objects.all():
    print(b)

# Retrieve a random book from model and print it.
class_count = Class.objects.count()
class_ = Class.objects.all()[fake.random_int(0, class_count - 1)]

print("\nExample Book:")
print(f"Title: {class_.title}")
print(f"Author: {class_.professor}")
print(f"Summary:\n{textwrap.fill(class_.summary, 77)}")


username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080"
====================================================================
"""
print(message)
