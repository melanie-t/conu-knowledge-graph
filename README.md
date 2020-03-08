# COMP474_A1_W20

Setting Up DBPedia Spotlight Server</br>
1. Download the files below into the project's main directory (/COMP474_A1_W20/)</br>
[DBPedia Spotlight](https://sourceforge.net/projects/dbpedia-spotlight/files/spotlight/dbpedia-spotlight-1.0.0.jar/download) (190MB) </br>
[DBPedia Spotlight Model (2016-10/en)](https://sourceforge.net/projects/dbpedia-spotlight/files/2016-10/en/model/en.tar.gz/download) (1.8 GB)
2. Navigate to the project directory extract the model by running ```server_1_extract_en.sh``` </br>

3. Run ```server_2_init.sh``` to start the server.</br>
4. When the server has been initialized, run ```server_3_test.sh``` to test that the server is running. It should return annotations.</br>

Setting up the Project
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
