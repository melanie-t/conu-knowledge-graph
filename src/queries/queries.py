"""
Write  SPARQL  queries  that  retrieve  the  following  information  from  yourknowledge base:

 Total number of triples in the KB
 Total number of students, courses, and topics
 For a course c, list all covered topics using their (English) labels and their link to DBpedia
 For a given student, list all courses this student completed, together with the grade
 For a given topic, list all students that are familiar with the topic (i.e., took, and did not fail, acourse that covered the topic)
 For a student, list all topics (no duplicates) that this student is familiar with (based on the completedcourses for this student that are better than an “F” grade)

"""
from rdflib import Graph

g = Graph()
g.parse("../rdfPopulator/output.ttl", format="turtle")

print(len(g))
q1 = open("q1.txt", "r")
q1_response = open("q1_response.txt", "w")

query = q1.read() #Not working in query
print(query)

# Counts the nb of triples in the KB
res1 = g.query("""
    SELECT (COUNT(*) as ?Triples)
    WHERE{?s ?p ?o .}
""")

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
