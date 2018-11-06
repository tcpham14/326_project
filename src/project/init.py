import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker
import random

from spew.models import Professor, User, Feedback, Subject, Class

fake = Faker()

# Delete all pre-existing objects
Professor.objects.all().delete()
Feedback.objects.all().delete()
Subject.objects.all().delete()
Class.objects.all().delete()
User.objects.all().delete()

# Create Genres
subjects = [
    Subject(subject_name="Computer Science"),
    Subject(subject_name="Mathematics"),
    Subject(subject_name="Chemistry"),
    Subject(subject_name="Physics"),
    Subject(subject_name="English"),
    Subject(subject_name="Nutrition"),
    Subject(subject_name="Finance"),
    Subject(subject_name="Music"),
    Subject(subject_name="Accounting"),
    Subject(subject_name="History"),
    Subject(subject_name="Food Science"),
    Subject(subject_name="Public Health"),
    Subject(subject_name="Journalism"),
    Subject(subject_name="Kinesiology"),
    Subject(subject_name="Microbiology"),
    Subject(subject_name="Sports Management"),
    Subject(subject_name="Philosophy"),
]

concentrations = [

    [
    'Software Engineering',
    'Artificial Intelligence',
    'Networking',
    'Theory of Computation',
    'Search & Data Mining',
    'Computer Architechure'
    ],

    [
    'Scientific Computing',
    'Mathematical Economics',
    'Mathematical Education'
    ],

    [
    'Chemical Biology ',
    'Environmental Chemistry',
    'Materials/Industrial Chemistry'
    ]

]

# OUTER NEST = SUBJECT AS PER ORDER OF subjects[] above
# INNER NEST = COURSE WITHIN THAT SUBJECT
#[Title, Code, Credits, Exams, Attendence, Textbooks]
courses_list = [
    [
    ["Introduction to Programming", 119, 3, 'Yes', 'Mandatory', 'None'],
    ["Introduction to Problem Solving with Computers", 121, 4, 'Yes', 'Not Required', 'None'],
    ["Programming with Data Structures", 187, 4, 'Yes', 'Not Required', 'None'],
    ["Programming Methodology", 220, 4, 'None', 'Not Required', 'None'],
    ["Computer Systems Principles", 230, 4, 'Yes', 'Mandatory', 'None'],
    ["Reasoning Under Uncertainty", 240, 4, 'Yes', 'Not Required', 'None'],
    ["Introduction To Computation", 250, 4, 'Yes', 'Mandatory', 'None'],
    ["Introduction to Algorithms", 311, 4, 'Yes', 'Not Required', 'None'],
    ["Software Engineering", 320, 4, 'None', 'Mandatory', 'None'],
    ["Web Programming", 326, 4, 'None', 'Mandatory', 'None'],
    ["Practice and Applications of Data Management", 345, 3, 'Yes', 'Mandatory', 'None']
    ],

    [
    ["Calculus for the Life and Social Sciences I", 127, 3, 'Yes', 'Not Required', 'None'],
    ["Calculus for the Life and Social Sciences II", 128, 3, 'Yes', 'Not Required', 'None'],
    ["Calculus I", 131, 4, 'Yes', 'Not Required', 'None'],
    ["Calculus II", 132, 4, 'Yes', 'Not Required', 'None'],
    ["Multivariate Calculus", 233, 3, 'Yes', 'Not Required', 'None'],
    ["Introduction to Linear Algebra", 235, 3, 'Yes', 'Not Required', 'None'],
    ["Statistics I", 515, 3, 'Yes', 'Not Required', 'None'],
    ["Statistics II", 516, 3, 'Yes', 'Not Required', 'None']
    ],

    [
    ["Gen Chem-Sci", 111, 4, 'Yes', 'Not Required', 'None'],
    ["Gen Chem-Sci", 112, 4, 'Yes', 'Not Required', 'None'],
    ["Organic Chemistry", 250, 4, 'Yes', 'Mandatory', 'None'],
    ["Quant Analysis", 315, 4, 'Yes', 'Mandatory', 'None'],
    ["Physical Chem", 476, 3, 'Yes', 'Mandatory', 'None'],
    ["Physical Biochemistry", 728, 3, 'Yes', 'Mandatory', 'None'],
    ]
]

# OUTER NEST = SUBJECT AS PER ORDER OF subjects[] above
# INNER NEST = COURSE WITHIN THAT SUBJECT
course_descriptions = [
    [
    "An introduction to computer programming with multimedia applications. Students will create Python programs to process image, video, and audio data. No prior programming experience expected. Not open to Computer Science majors.",
    "An introductory course in problem solving, using the programming language Java. Focuses on the fundamental concepts of problem solving and on computer implementation. Intended for computer science majors or those applying for the major. Satisfactory completion is a prerequisite for all higher-level computer science courses. Use of a laptop computer required. Prerequisite: high school algebra and basic math skills (R1).  (Gen.Ed. R2)",
    "This course introduces and develops methods for designing and implementing abstract data types using the Java programming language. The main focus is on how to build and encapsulate data objects and their associated operations. Specific topics include linked structures, recursive structures and algorithms, binary trees, balanced trees, and hash tables. These topics are fundamental to programming and are essential to other courses in computer science. The course involves weekly programming assignments, in-class quizzes, discussion section exercises, and multiple exams.",
    "Development of individual skills necessary for designing, implementing, testing and modifying larger programs: use of various modern automated tools, design strategies and patterns, working with large code bases and libraries, code refactoring.",
    "Large-scale software systems like Google - deployed over a world-wide network of hundreds of thousands of computers - have become a part of our lives. These are systems success stories - they are reliable, available (up nearly all the time), handle an unbelievable amount of load from users around the world, yet provide virtually instantaneous results. On the other hand, many computer systems don't perform nearly as well as Google - hence the now-cliche the system is down. In this class, we study the scientific principles behind the construction of high-performance, scalable systems. The course begins with a discussion of the relevant features of modern architectures, and moves up the stack from there to operating system services such as programming language runtime systems, concurrency and synchronization, with a focus on key operating system features, I/O and networking, and distributed services.",
    "Development of mathematical reasoning skills for problems that involve uncertainty. Counting and probability -- basic counting problems, probability definitions, mean, variance, binomial distribution, discrete random variables, continuous random variables, Markov and Chebyshev bounds, Laws of large number, and central limit theorem. Probabilistic reasoning -- conditional probability and odds, Bayes' Law, Markov Chains, Bayesian Network, Markov Decision Processes.",
    "Basic concepts of discrete mathematics useful to computer science:  set theory, strings and formal languages, propositional and predicate calculus, relations and functions, basic number theory.  Induction and recursion:  interplay of inductive definition, inductive proof, and recursive algorithms.  Graphs, trees, and search.   Finite-state machines, regular languages, nondeterministic finite automata, Kleene's Theorem.  Problem sets, 2 midterm exams, timed final.",
    "The design and analysis of efficient algorithms for important computational problems. Emphasis on the relationships between algorithms and data structures and on measures of algorithmic efficiency. Sorting (heapsort, mergesort, quicksort), searching, graph algorithms. Experimental analysis of algorithms also emphasized. Use of computer required.",
    "In this course, students learn and gain practical experience with software engineering principles and techniques. The practical experience centers on a semester-long team project in which a software development project is carried through all the stages of the software life cycle. Topics in this course include requirements analysis, specification, design, abstraction, programming style, testing, maintenance, communication, teamwork, and software project management. Particular emphasis is placed on communication and negotiation skills and on designing and developing maintainable software.  Use of computer required. Several written assignments, in-class presentations, and a term project. This course satisfies the Integrative Experience requirement for BS and BA CS majors.",
    "The World Wide Web was proposed originally as a collection of static documents inter-connected by hyperlinks. Today, the web has grown into a rich platform, built on a variety of protocols, standards, and programming languages, that aims to replace many of the services traditionally provided by a desktop operating system.  This course will study core technologies, concepts, and techniques behind the creation of modern web-based systems and applications.  This course satisfies the Integrative Experience requirement for BS/BA CS majors.",
    "Practice and Applications of Data Management"
    ],

    [
    "Basic calculus with applications to problems in the life and social sciences. Functions and graphs, the derivative, techniques of differentiation, curve sketching, maximum-minimum problems, exponential and logarithmic functions, exponential growth and decay, and introduction to integration. Prerequisite: proficiency in high school algebra, including word problems. Honors sections available.  (Gen.Ed. R2) ",
    "Continuation of MATH 127. Elementary techniques of integration, introduction to differential equations, applications to several mathematical models in the life and social sciences, partial derivatives, and some additional topics. Prerequisite: MATH 127.  (Gen.Ed. R2) ",
    "Continuity, limits, and the derivative for algebraic, trigonometric, logarithmic, exponential, and inverse functions. Applications to physics, chemistry, and engineering. Prerequisites: high school algebra, plane geometry, trigonometry, and analytic geometry. Honors section available first semester.  (Gen.Ed. R2)",
    "The definite integral, techniques of integration, and applications to physics, chemistry, and engineering. Sequences, series, and power series. Taylor and MacLaurin series. Prerequisite: MATH 131 or equivalent. Honors section available.  (Gen.Ed. R2)",
    "Techniques of calculus in two and three dimensions. Vectors, partial derivatives, multiple integrals, line integrals. Honors section available.  (Gen.Ed. R2)",
    "Basic concepts of linear algebra. Matrices, determinants, systems of linear equations, vector spaces, linear transformations, and eigenvalues. Prerequisite or corequisite: MATH 132, or 136, or consent of instructor.  (Gen.Ed. R2) ",
    "First semester of a two-semester sequence. Emphasis given to probability theory necessary for application to and understanding of statistical inference. Probability models, sample spaces, conditional probability, independence. Random variables, expectation, variance, and various discrete and continuous probability distributions. Sampling distributions, the Central Limit Theorem and normal approximations. Multivariate calculus introduced as needed. Prerequisites: MATH 132, or 136.  (Gen.Ed. R2) ",
    "Basic ideas of point and interval estimation and hypothesis testing; one and two sample problems, simple linear regression, topics from among one-way analysis of variance, discrete data analysis and nonparametric methods.  Prerequisite: Statistc 515 or equivalent. "
    ],

    [
    "Basic principles of structure and reactivity. Microscopic nature of atoms and molecules; the macroscopic properties of chemical systems. Topics include stoichiometry, thermochemistry, atomic structure, molecular structure, properties of gases. (Gen.Ed. PS) ",
    "Continuation of CHEM 111. States of matter, solutions, thermodynamics, equilibrium, kinetics, oxidation-reduction processes, and electrochemical cells.  (Gen.Ed. PS)",
    "A one-semester introduction to chemistry of organic compounds: alkanes, alkenes, alkynes, aromatic compounds, alkyl halides, alcohols, ethers, aldehydes and ketones, carboxylic acids and their derivatives, phenols, amines, fats, amino acids, carbohydrates. Emphasizes nomenclature, structure, synthesis, stereochemistry, mechanisms of organic reactions.  Prerequisite: CHEM 110 or 111 or equivalent.",
    "Fundamental principles of quantitative analytical chemistry with practical inorganic and organic applications. Includes titrimetric methods, acid-base, complexometric and redox, plus separation, electrochemical, and spectroscopic techniques.",
    "Introduction to the laws controlling equilibrium and kinetic properties of macroscopic chemical systems, using thermodynamics and statistical mechanics.  Prerequisites:  CHEM 475",
    "Chemical, physical, and biological properties of proteins and nucleic acids. Macromolecular structure of biopolymers; optical, hydrodynamic, and magnetic resonance techniques; multiple equilibria; relaxation kinetics, and conformational transitions.",
    ]
]

# Comments in the order of ratings(1.0-5.0)
comments = [
    "The worst class ever. Too much homework that takes way too much time to do",
    "A very difficult class with a teacher that rushes through the material way too quickly",
    "Very unforgiving grade scale",
    "Hard material with an even harder teacher",
    "Amazingly smart guy and is really charming. The homework can be overwhelming but the exams are not as bad. Prepare to work really hard especially because of the raw amount of material covered in class.",
    "The homework problems are very specific, and took a lot of time. However, they were rewarding once you managed to solve them yourself.",
    "Great guy, super smart. Put in the work, you will learn. If discrete math/proofs aren't your thing you will have to work really hard or you will struggle hard in the course.",
    "His lectures can be a bit dry and very dense but he is very kind and will answer any questions.",
    "There's tons of work so you'll want to start the HW early and compare with other people for sure. The scale at the end of the semester is pretty forgiving too.",
    "A very difficult class but you will actually learn",
    "The textbook is written by him and is very concise, but you need to work hard, pay attention at all times and put in work after class to pass",
    "Great professor that genuinely wants to help the students learn",
    "A very smart teacher teaching a very difficult class"
]


# Save the genres to the database
for subject in subjects:
    subject.save()

#############################################
###### CREATION OF PROFESSOR OBJECTS ########
#############################################
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
######################################
##### CREATION OF CLASS OBJECTS ######
######################################
# Iterate through each subject(0 -> 2)
for subject_index in range(0, 3):
    classes.append([])
    # Iterate through each course in that subject (0 -> len)
    for course_index in range (0, len(courses_list[subject_index])):
        # Create all class fields
        c_subject = subjects[subject_index]
        c_code = courses_list[subject_index][course_index][1]
        c_id = int(str(subject_index) + str(course_index))
        c_title = courses_list[subject_index][course_index][0]
        c_professor = professors[fake.random_int(0, len(professors)) - 1]
        c_description = course_descriptions[subject_index][course_index]
        c_exams = courses_list[subject_index][course_index][3]
        c_attendance = courses_list[subject_index][course_index][4]
        c_textbooks = courses_list[subject_index][course_index][5]
        c_credits = courses_list[subject_index][course_index][2]
        # Create class object and populated with c_ parameters
        course = Class(class_id = c_id, title=c_title, code = c_code, num_credits = c_credits, professor=c_professor, description=c_description,
            exams=c_exams, attendance = c_attendance, textbooks = c_textbooks, subject = c_subject)
        course.save()
        # Append to nested classes list
        classes[subject_index].append(course)


###################################################################################
##### MAPPING OF EACH CLASS OBJECT TO OTHER CLASS OBJECTS AS RELATED CLASSES ######
###################################################################################
# For each subject
for subject_name in classes:
    course2_start_index = 0
    # For each course
    for course1 in subject_name:
        # course2_start_index incremented by 1 to prevent course1 from adding itself
        # as a related class
        course2_start_index = course2_start_index + 1
        # Shuffle the list of courses
        subject_name_shuffled = subject_name[course2_start_index:].copy()
        random.shuffle(subject_name_shuffled)
        # Add every other course in the same subject as a related course
        for course2 in subject_name_shuffled:
            if(course1.title != course2.title):
                course1.related_classes.add(course2)


######################################
##### CREATION OF USER OBJECTS #######
######################################
users = []
for i in range(1,10):
    subject_index = fake.random_int(0, 2)
    u_fname = fake.first_name()
    u_lname = fake.last_name()
    u_user_id = i
    u_bio = fake.text(500)
    u_grad_year = fake.year()
    u_major = subjects[subject_index]
    u_concentration = concentrations[subject_index][fake.random_int(1, len(concentrations[subject_index])-1)]
    u_liked_reviews = fake.random_int(0, 30)
    u_classes_taken = fake.random_int(0, 30)
    user = User(first_name = u_fname, last_name = u_lname, user_id = u_user_id, grad_year = u_grad_year, bio = u_bio, major = u_major, concentration = u_concentration, num_classes_taken = u_classes_taken, num_liked_reviews = u_liked_reviews)
    user.save()

    num_fav_courses = fake.random_int(1, len(classes[subject_index])-1)
    num_current_courses = fake.random_int(4, len(classes[subject_index])-1)
    
    used_fav_courses = []
    for x in range(0, num_fav_courses):
        course_index = fake.random_int(0, len(classes[subject_index])-1)
        if course_index in used_fav_courses:
            continue
        user.fav_courses.add(classes[subject_index][course_index])
        used_fav_courses.append(course_index)

    used_current_courses = []
    for x in range(0, num_current_courses):
        course_index = fake.random_int(0, len(classes[subject_index])-1)
        if course_index in used_current_courses:
            continue
        user.current_courses.add(classes[subject_index][course_index])
        used_current_courses.append(course_index)

    user.save()
    users.append(user)


##########################################
###### CREATION OF FEEDBACK OBJECTS ######
##########################################
# feedbacks[] currently not used, no point to keep track of feedback through array
# when feedback for a class is accessible through classes[x][y].course_feedback.all()
feedbacks = []
# Iterate through each subject(0 -> 2)
for subject_index in range(0, 3):
    # Iterate through each course in that subject (0 -> len)
    for course_index in range (0, len(courses_list[subject_index])):
        # Store pre-fabricated comments used from comments[] into
        # used_comments so that there are no duplicates comments for each class
        used_comments = []
        used_users = []
        # Each class will have a random number of reviews num_reviews
        num_reviews = random.randint(1, 10)
        for review in range(0, num_reviews):
            # Map the randomly generated rating to a comment that matches the rating
            r_int = random.randint(1,5)
            u_int =random.randint(0,len(users)) - 1
            str(r_int)
            if(r_int == "1" or r_int == "2"):
                r2_int = random.randint(0,3)
            elif(r_int == "3" or r_int == "4"):
                r2_int = random.randint(4,8)
            else:
                r2_int = random.randint(9,12)  
            if r2_int in used_comments or u_int in used_users:
                continue
            c_comment = comments[r2_int]
            c_course = classes[subject_index][course_index]
            c_user = users[u_int]
            c_date = fake.date_this_decade(before_today=True, after_today=False)
            # Create the feedback submission
            submission = Feedback(date = c_date, comment = c_comment, course = c_course, user = c_user, rating = r_int)
            submission.save()
            #feedbacks.append(submission)
            # Add current feedback submission to the current class to reference
            # when rendering class page
            used_comments.append(r2_int)
            used_users.append(u_int)









################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################













# Retrieve a random book from model and print it.
class_count = Class.objects.count()
class_ = Class.objects.all()[fake.random_int(0, class_count - 1)]

'''print("\nExample Book:")
print("Title: {class_.title}")
print("Author: {class_.professor}")
print("Summary:\n{textwrap.fill(class_.summary, 77)}")'''


'''username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()'''
message = "Success"
"""
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
