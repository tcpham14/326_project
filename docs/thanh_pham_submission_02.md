For this project, I was able to create and change fields for certain models, such as figuring out how to reverse-reference a foreign key and create a many-many field that allows a model to reference itself.

Additionally, I was able to populate a portion of the init.py file with mock data and actual data from SPIRE for classes/professors/subjects, such as a class's description, credits, etc. This data is passed as context for the template that we render for each page.

I also was able to create multiple views for certain pages and render particular context to that page's template that was filtered (such as which classes are related to a particular class, which classes a professor tecaches, etc.) and compute the average rating / most ratings for each class.

The biggest challenge that I encounted personally was working with multiple other people at the same time while we are constantly pushing and pulling and modifying files, especially since I was still a beginner at using git from the command line. A lot of the time we would encounter merge conflicts while overwriting files untentionally. 