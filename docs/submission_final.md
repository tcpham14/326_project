Title: Weebs


Subtitle: Spew


Semester: Fall 2018


Overview: Spew is an innovative student-driven database centered around finding the perfect class for any student. It provides an array of information on any class offered at UMass, such as required textbooks, instructors, attendance and so on. It also allows students to share feedback in the form of reviews, along with ratings based on certain disciplines of the class. This application will allow students to view most-rated and highest-rated classes, along with the ability to view related classes in the form of track based on the student's concentration. Students will also have the ability to look into what courses other students are taking, along with other information such as their major, graduation year, and biography.


Team Members: Lucas Phan, Thanh Pham, Nhi Lam, Richard Li, Taesan Yoon, Michael Ahn


User Interface: Each page of our UI is fairly self-explanatory. We have a persistent nav bar at the top that has links to each of the views.

Home Page / Landing Page
![example image](images_final/326HomePage.png)
Registration Page
![example image](images_final/326RegistrationPage.png)
Login Page
![example image](images_final/326LoginPage.png)
Class Page - Contains all of the fine details of each class
![example image](images_final/326ClassPage.png)
Class List Page - Lists all of the available classes
![example image](images_final/326ClassList.png)
Professor Page - Contains all of the fine details of each professor
![example image](images_final/326ProfessorPage.png)
Professor List Page - Lists all of the professors
![example image](images_final/326ProfessorList.png)
Student Page - Contains all of the fine details of each student
![example image](images_final/326StudentPage.png)
Student List Page - Lists all of the students
![example image](images_final/326StudentList.png)
Edit Profile Page - Only accessible for your own user page
![example image](images_final/326EditProfilePage.png)
Search Page - Currently not functional, but self-explanatory
![example image](images_final/326AdvancedSearch.png)
Search Results Page - Currently not functional, but self-explanatory
![example image](images_final/326SearchResultsPage.png)


Data Model:
![example image](images_final/Data_Model_Diagram.png)
For the entities in our models, we named them based on what they are used for, so the names themselves explain their relationships with the other models. For example, we have the Student model which contains the "fave_courses" entity that each student (user) can choose, which references the Class objects, and so on. The arrows from each model point to a model they have a direct relationship with.

URL Routes/Mappings: 

| Route               | Purpose                                                                                                        | 
|---------------------|----------------------------------------------------------------------------------------------------------------|
| users/              | Viewing the list of users on the website                                                                       |
| classes/            | Viewing the list of classes on the website                                                                     |
| professors/         | Viewing the list of professors on the website                                                                  |
| class/<int:pk>/     | Viewing the details of a class                                                                                 |
| user/<str:pk>/      | Viewing the details of a user                                                                                  |
| professor/<int:pk>  | Viewing the details of a professor                                                                             |
| search_results      | Viewing a list of classes based on a user’s certain criteria                                                   |
| advanced_search     | Allows user to find classes based on multiple forms of criteria                                                |
| accounts/register/  | A page allowing a person to register as a user of the website                                                  |
| accounts/login/     | A page that allows a person to log in. This route requires authentication of the user logging in               |
| submissions/create/ | Can create feedback for a class. A student only has permissions to create feedbacks for themselves             | 
| edit_profile/       | Allows user to edit their profile settings. A student only has permissions to edit their own profile           |

Authentication/Authorization: We have authentication for students only. Registration creates a User along with a Student (profile) which is a one-to-one model in relation to the User in order to add additional fields, basically extending the User model. The students, only once logged in, will be able to review classes (leave feedback and ratings). Users will only be able to access the edit profile for their own user profile page, not anyone else's. The user is also able to edit their password by going through the password reset form on the registration page. Only admins will be able to add classes and professors.


Team Choice: For our team choice, we added a "like" function for class feedback that is related. We added a "Like" model to our data model, which has three components: the student who liked the feedback, the feedback that is being liked, and a boolean field that shows if that student liked that feedback or not. In our views.py file, to our Class Detail View, we edited the look of the feedback given for that class on that page, adding a 'Like' counter and a 'like' button under each feedback. We initialize the likes in our init.py file by going through all the students and all the feedback, each 'liked' value being false for each student for each feedback until they click the like button, changing the value for that student for that feedback to 'true'.


Conclusion: This semester there were many things we as a team were able to learn  a website using django framework. On team level, we learned the importance of having clear and concise communication. When we were able to accomplish this feat, this made our work and progress much faster. We also learned the importance of always looking forward when making decisions and how our current design could affect things we would want to implement later. For instance, we tried to implement a custom user, but this caused issues later when we could not utilize django’s built in authentication with the custom user. In hindsight, it would have been better to use the default django user. All in all, the lessons that we learned will help us further our careers in computer science.
Throughout our project timeline we face many difficulties. One of the major difficulties that we faced was making group time when everyone was available. Every member in the group had a fairly busy schedule. So we were very fortunate when we could all find time to meet. Another, difficulty that we had was managing the github repo. It was very challenging at first to avoiding merge conflicts or making sure that we were adding helpful commits to our additions. 
We believe that if we took a crash course on how Github worked before starting this project, we could’ve avoided a lot of “who worked on what?” questions, as well as improved general folder organization. It was to our detriment that everyone in our group assumed that other people knew how Github worked. Knowing each others’ schedules and sharing them earlier on would also have improved our project experience, as scheduling conflicts were a frequent re-occurrence throughout the semester. Some technical issues we encountered were: computing average rating for a class and creating a custom spew user. We realized that in order to display the average rating for a class, we needed to consider the multiple feedback objects that went into the computation. For the custom spew user, we tried to go this route because of admin page errors. However, this conflicted with the django authentication that is given to the default user class.

