# TEAM WRITE-UP

# TEAM NAME
Weebs

# WEB APPLICATION NAME
Spew

# OVERVIEW
Spew is an innovative student-driven database centered around finding the perfect class for any student. It provides an array of information on any class offered at UMass, such as required textbooks, instructors, attendance and so on. It also allows students to share feedback in the form of reviews, along with ratings based on certain disciplines of the class. This application will allow students to view most-rated and highest-rated classes, along with the ability to view related classes in the form of track based on the student's concentration. 

# VIDEO LINK 
TODO

# DESIGN OVERVIEW
We have implemented several data points in our data model for Spew. We have the subject class, which includes the title of the subject. We have the Class class, which includes the title, code, description, textbooks, unique id, number of credits, a foreign key to subject, related classes (many to many from Class to itself), and boolean values of exams and attendance describing whether or not the class has exams and required attendance. We have the User class, which includes the first name, last name, major (a foreign key to subject), unique id, favorite courses (many to many to Class), current courses (many to many to Class), graduation year, number of classes taken, and number of liked reviews. We have the Professor class, which includes the first name, last name, position, contact information, office number, and courses taught by the Umass professor(many to many to Class). Finally, we have the Feedback class, which includes comments, date and ratings, as well as foreign keys for the user, professor, and class. 

For our important URL routes, we have paths for several web pages including: the class list page, class details page, a student profile page, the search results page, the submissions page, and the advanced search page. For each of these pages, we have the requests for the paths above, where Django would then call the views function for the particular path. We also have the name of the path for reference.

For the implemented UI views, they take web requests and respond with a web response. In our index.html file, or our home page, we have a variety of objects that are shown in the page. We have the number of classes, 4 classes that are featured randomly from a list of classes, 3 random feedbacks that correspond to the featured classes, a list of popular classes, a list of the highest rated classes, a list of the highest rated classes based on ratings, a list of the popular courses, and a list of the popular courses based on ratings. In addition, we implemented a generic list view for search results, the list of classes, and the list of users. We implemented a generic detail view for classes and users, where the user page shows feedback for the particular class and the user page shows feedbacks from the user, the number of feedbacks given, favorite courses, and current courses being taken. 
 
# SUCCESSES
* We have had success in creating an HTML template for each of our class pages and extending the base template
* We have had success in implementing Django in our design using views, templates, and urls
* We have had success in creating submission deadlines and staying consistent with them
# PROBLEMS
* Since many of us have not used GitHub to a great extent, we have had issues in the organization and of files and folders in the    project repo
* We have had issues in our ability to communicate as effectively
* We have had issues in finding time where everyone could meet and work together (scheduling conflicts)

