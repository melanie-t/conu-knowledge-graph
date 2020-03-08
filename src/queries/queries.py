"""
Write  SPARQL  queries  that  retrieve  the  following  information  from  your knowledge base:

 Total number of triples in the KB
 Total number of students, courses, and topics
 For a course c, list all covered topics using their (English) labels and their link to DBpedia
 For a given student, list all courses this student completed, together with the grade
 For a given topic, list all students that are familiar with the topic (i.e., took, and did not fail, acourse that covered the topic)
 For a student, list all topics (no duplicates) that this student is familiar with (based on the completedcourses for this student that are better than an “F” grade)

"""
from rdflib import Graph
import os
import errno

# Source: https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory/14364249#14364249
# And https://github.com/melanie-t/COMP472_Project1_W20/blob/master/src/helper_functions.py
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
# End source

g = Graph()
g.parse("../rdfPopulator/output.ttl", format="turtle")

print(len(g))
make_sure_path_exists("./sparql_queries")
make_sure_path_exists("./output")

file_query = "q1.txt"
file_output = "q1_response.txt"

q1 = open("./sparql_queries/"+file_query, "r")
q1_response = open("./output/"+file_output, "w")

# Counts the nb of triples in the KB
res1 = g.query(q1.read())

res2 = g.query("""
    SELECT 
        (COUNT(?student) as ?studentsCount) 
        (COUNT(?course) as ?courseCount) 
        (COUNT(?topic) as ?topicCount)
    WHERE{
        ?student a <http://www.example.org/student/Student> .
        ?course a <http://www.example.org/course/Course> .
        ?topic a <http://www.example.org/course/CourseAcronym> .
    }
    """)


course = "EDUC/399"
res3 = g.query("""
    SELECT ?grade ?courses ?student
    WHERE{
        ?student ns3:enrolled_to ?course .
        ?student ns3:completed_with ?grade .
    }
""")

for row in res1:
    q1_response.write(row[0])

for row in res2:
    for i in range(3):
        print(row[i])
"""

      res2 = g.query(
    SELECT (COUNT(*) as ?studentsCount) (COUNT(*) as ?courseCount) (COUNT(*) as ?topicCount)
    WHERE{
        ?student a <http://www.example.org/student/Student> .
        ?course a <http://www.example.org/course/Course> .
        ?topic a <http://www.example.org/course/CourseAcronym> .
    }
    )

        
        
SELECT  ?s ?c ?t
WHERE{
    ?s = 
}
"""
