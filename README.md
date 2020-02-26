# COMP474_A1_W20
Setting Up The Project
1. Clone the repository
2. Navigate to COMP474_A1_W20\venv\pyvenv.cfg
	Change home directory to your Python installation </br>
    (Ex: home=C:\Program Files\Python38)
3. Open the COMP474_A1_W20 folder as a PyCharm folder
4. Add an existing interpreter </br>
	File -> Settings -> Project: COMP474_A1_W20 -> Project Interpreter -> Top right cog -> Add -> Virtualenv Environment -> Existing Environment -> [...] -> [...]\COMP474_A1_W20\venv\Scripts\python.exe (Navigate to project repo)


The courseExtraction module gets all the HTML pages from the Concordia website (CourseDataCollector.py). It then parses the data (the htmls) to extract the courses from each web page (CourseExtractionMain.py). Then, we can reach for these courses as a 'Course' object list from the script CourseExtractorFromTxt.py.

The spotlightAnnotations module gives a basic method to get back every term in a block of text that DBpedia has linked to their database. It comes with the term, and the link. There are also two other methods that attempt to put all those terms/links into a file, but due to the API limitations, I was not able to.

The studentCreation module creates the Student objects along with all the information related to the courses they have taken.

The rdfPopulator module create the RDF schema using the Turtle format. The script ttlCreator.py contains all the necessary information. The RDF schema can be found in rdfPopulator/output.ttl
