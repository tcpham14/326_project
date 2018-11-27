Taesan Yoon write up

One aspect of this project that I contribute to was finding mock data for comments and ratings on Rate my Professor that pertained to the 
Feedback class and stored them in init.py.I created a method that randomly chose a rating from 1-5 (1 to 5 stars for rating) and chose 
corresponding random comments depending on how low or high the ratings were. If the rating was 1-2, a poorly written comment was randomly 
chosen. If the rating was 3-4, a mediocre written comment was randomly chosen. If the rating was 5, a great written comment was randomly chosen.

Another aspect of this project that I contributed to was the data diagram. I created a mock data diagram on a piece of paper, and I focused on making sure 
everything in the model made sense as I was filling out the final diagram. Specifically, I came across an error that needed fixing. There was a many to many relationship
outlined in the Class class to Feedback, while also being a one to many (foreign key) relationship outlined in the Feedback class to Class. It made sense to the have the
one to many relationship, so we got rid of the many to many relationship and made appropriate changes to the rest of the model.

A final aspect of this project that I contributed towards was the team write up. For this piece of the project I think the biggest challenge was I needed to know what 
was going on in terms of the bigger picture of how the views, urls, and data models came together. A lot of the strengths and weaknesses of the group was easy to determine 
while observing the group, and our idea of where the project was going stayed generally the same. 


