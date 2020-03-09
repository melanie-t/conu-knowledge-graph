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


def create_prefix():
    prefix_list = ''
    # Import prefixes from ttl
    try:
        # Source: https://stackabuse.com/read-a-file-line-by-line-in-python/
        filepath = '../rdfPopulator/output.ttl'
        with open(filepath) as f:
            line = f.readline()
            prefix_list = prefix_list + line
            cnt = 1
            while line:
                line = f.readline()
                if line in ['\n', '\r\n']:
                    break
                prefix_list = prefix_list + line
                cnt += 1
    finally:
        f.close()

    prefix_list = prefix_list.replace("@prefix", "PREFIX")
    prefix_list = prefix_list.replace(" .", "")

    return prefix_list


if __name__ == '__main__':
    prefix = create_prefix()
    g = Graph()
    g.parse("../rdfPopulator/output.ttl", format="turtle")

    # Query 1. Total number of triples in the KB
    file_query = "q1.txt"
    file_output = "q1_response.txt"
    q1 = open("./sparql_queries/" + file_query, "r")
    q1_response = open("./output/" + file_output, "w")

    res1 = g.query(prefix + q1.read())

    for row in res1:
        q1_response.write(row[0])

    # Query 2. Total number of students, courses, and topics
    # TODO: DOES NOT WORK
    """
    SELECT (COUNT(*) as ?studentsCount) (COUNT(*) as ?courseCount) (COUNT(*) as ?topicCount)
    WHERE {
        ?student a <http://www.example.org/student/Student> .
        ?course a <http://www.example.org/course/Course> .
        ?topic a <http://www.example.org/course/CourseAcronym> .
    }
    """

    # Query 3. For a course c, list all covered topics using their (English) labels and their link to DBpedia
    # TODO: Waiting for Course Code to display
    """
    SELECT ?completed_course ?grade
    WHERE {
        ?student a student:Student .
        ?student exprop:identified_by "422222" .
        ?student exprop:enrolled_in ?completed_course .
        ?completed_course exprop:completed_with ?grade .
    }
    """
    q3 = open("./sparql_queries/" + "q3.txt", "r")
    q3_response = open("./output/" + "q3_response.txt", "w")

    res3 = g.query(prefix + q3.read())
    for row in res3:
        q3_response.write(row['completed_course'], row['grade'])

    # Query 4. For a course c, list all covered topics using their (English) labels and their link to DBpedia
    """
    SELECT ?label ?topic
    WHERE {
        <http://www.example.org/course/ACCO/220> sioc:topic ?topic .
        ?topic rdfs:label ?label .
    }
    """
    q4 = open("./sparql_queries/" + "q4.txt", "r")
    q4_response = open("./output/" + "q4_response.txt", "w")

    res4 = g.query(prefix + q4.read())
    for row in res4:
        for entity in row:
            q4_response.write(entity + "\t")
        q4_response.write("\n")


    # Query 5. For a given topic, list all students that are familiar with the topic (i.e., took, and did not fail, acourse that covered the topic)
    # TODO

    # Query 6.For a student, list all topics (no duplicates) that this student is familiar with (based on the completedcourses for this student that are better than an “F” grade)
    # TODO

