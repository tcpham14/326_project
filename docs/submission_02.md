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
We have implemented several data points in our data model for Spew. We have the subject class, which takes a CharField of the particular subject of a Umass class. We have the Class class, which includes the title, code, description, textbooks, unique id, and boolean values of exams and attendance describing whether or not the class has exams and required attendance. We have the User class, which includes the first name, last name, major, unique id, and courses that were taken by the student. We have the Professor class, which includes the first name, last name, position, contact information, office number, and courses taught by the Umass professor. Finally, we have the Feedback class, which includes comments and ratings, as well as foreign keys for the user that issued the comment and the class that it was for. 

For our important URL routes, we have paths for several web pages including: the class list page, class details page, a student profile page, the search results page, the submissions page, and the advanced search page. For each of these pages, we have the requests for the paths above, where Django would then call the views function for the particular path. We also have the name of the path for reference.

For the implemented UI views, TODO
 
# SUCCESSES
* We have had success in creating an HTML template for each of our class pages and extending the base template
* We have had success in implementing Django in our design using views, templates, and urls
* We have had success in creating submission deadlines and staying consistent with them
# PROBLEMS
* Since many of us have not used GitHub to a great extent, we have had issues in the organization and of files and folders in the project repo
* We have had issues in our ability to communicate as effectively
* We have had issues in finding time where everyone could meet and work together (scheduling conflicts)

