# COMP474 Project 2

# The Project
The purpose of this project is to create a chatbot for Concordia University that is able to answer questions relating to courses, topics and students that are enrolled in Concordia University. The courses are added to the knowledge graph automatically using Concordia University's website.

# Part I - Creation of Knowledge Graph
## Setting Up DBPedia Spotlight Server</br>
1. Download the files below into the project's main directory (/COMP474_A1_W20/)</br>
[DBPedia Spotlight](https://sourceforge.net/projects/dbpedia-spotlight/files/spotlight/dbpedia-spotlight-1.0.0.jar/download) (190MB) </br>
[DBPedia Spotlight Model (2016-10/en)](https://sourceforge.net/projects/dbpedia-spotlight/files/2016-10/en/model/en.tar.gz/download) (1.8 GB)
2. Navigate to the project directory and run ```server_1_extract_en.sh``` to extract the model</br>
3. Run ```server_2_init.sh``` to start the server.</br>
4. (Optional) When the server has been initialized, run ```server_3_test.sh``` to test that the server is running. It should return annotations.</br>

## Setting up the Project using Virtual Environment (venv)
1. Clone the repository
2. Navigate to conu-knowledge-graph\venv\pyvenv.cfg
	* Change home directory to your Python installation </br>
    (Ex: home=C:\Program Files\Python38)
3. Open the conu-knowledge-graph folder as a PyCharm folder
4. Add an existing interpreter </br>
	File -> Settings -> Project: conu-knowledge-graph -> Project Interpreter -> Top right cog -> Add -> Virtualenv Environment -> Existing Environment -> [...] -> [...]\conu-knowledge-graph\venv\Scripts\python.exe

## Modules
The courseExtraction module gets all the HTML pages from the Concordia website (`CourseDataCollector.py`). It then parses the data (the htmls) to extract the courses from each web page (`CourseExtractionMain.py`). Then, we can reach for these courses as a 'Course' object list from the script `CourseExtractorFromTxt.py`.

The spotlightAnnotations module gives a basic method to get back every term in a block of text that DBpedia has linked to their database. It comes with the term, and the link. There are also two other methods that attempt to put all those terms/links into a file, but due to the API limitations, I was not able to.

The studentCreation module creates the Student objects along with all the information related to the courses they have taken.

The rdfPopulator module create the RDF schema using the Turtle format. The script `ttlCreator.py` contains all the necessary information. The RDF schema can be found in rdfPopulator/output.ttl

# Part II - ChatBot
## Starting ConU ChatBot
1. Once the project has been properly set up (from Part I), run `ChatbotMain.py`
2. Enter a question for ConU ChatBot to answer. <br>The following questions are currently supported:
	1.	What's COMP 474 about?
	2.	Which courses did Bianca Patry take?
	3.	Which courses cover Natural Language Processing?
	4.	Who is familiar with Education?
3. The results are outputted after querying our knowledge graph (`output.ttl`)
