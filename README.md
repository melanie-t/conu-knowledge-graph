# COMP474_A1_W20
Setting Up The Project
1. Clone the repository
2. Navigate to COMP474_A1_W20\venv\pyvenv.cfg
	Change home directory to your Python installation (Ex: C:\Program Files\Python38)
3. Open the COMP474_A1_W20 folder as a PyCharm project
4. Add an existing interpreter </br>
	File -> Settings -> Project: COMP474_A1_W20 -> Project Interpreter -> Top right cog -> Add -> Virtualenv Environment -> Existing Environment -> [...] -> [...]\COMP474_A1_W20\venv\Scripts\python.exe (Navigate to project repo)

Version: Python 3.8

Division of Tasks
1. Create RDF Schema - We have to create the schema and add triples to populate data. For Courses and Topics, they have to be automatically generated from https://www.concordia.ca/academics/graduate/calendar/current/encs/computer-science-courses.html
	- (Guenole) Universities
	- (Walid) Courses
	- (Melanie) Topics extracted from Courses + URI 
	- (Alex) Students (min. 10)
2. (Walid + Melanie) Automated Knowledge Base Construction
3. (Guenole + Alex) Knowledge Base Queries (#1-#6)
4. (All) Report
