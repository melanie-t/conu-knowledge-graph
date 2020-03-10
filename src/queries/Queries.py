import os
import errno
from rdflib import Graph


class Q1:
    # 1. Total number of triples in the KB
    @staticmethod
    def query(prefix, graph):
        query_num = "q1"
        query, output = open_query_files(query_num)
        query_string = query.read()
        query_string = prefix + query_string
        print("Query 1\n" + query_string)

        construct_results = Graph()
        results = graph.query(query_string)
        save_results(results, output)


class Q2:
    # 2. Total number of students, courses, and topics
    @staticmethod
    def query(prefix, graph):
        query_num = "q2"
        query, output = open_query_files(query_num)
        query_string = query.read()
        query_string = prefix + query_string
        print("Query 2\n" + query_string)

        construct_results = Graph()
        results = graph.query(query_string)
        save_results(results, output)


class Q3:
    # 3. For a course c, list all covered topics using their (English) labels and their link to DBpedia
    @staticmethod
    def query(course_uri, prefix, graph):
        query_num = "q3"
        query, output = open_query_files(query_num)
        query_string = query.read()
        query_string = query_string.replace("{course_uri}", str(course_uri))
        query_string = prefix + query_string
        print("Query 3\n" + query_string)

        construct_results = Graph()
        results = graph.query(query_string)
        save_results(results, output)


class Q4:
    # 4. For a given student, list all courses this student completed, together with the grade
    @staticmethod
    def query(student_id, prefix, graph):
        query_num = "q4"
        query, output = open_query_files(query_num)
        query_string = query.read()
        query_string = prefix + query_string
        # Replace values
        query_string = query_string.replace("{student_id}", str(student_id))
        print("Query 4\n" + query_string)

        construct_results = Graph()
        results = graph.query(query_string)
        save_results(results, output)


class Q5:
    # 5. For a given topic, list all students that are familiar with the topic (i.e., took,
    # and did not fail, a course that covered the topic
    @staticmethod
    def query(topic_uri, prefix, graph):
        query_num = "q5"
        query, output = open_query_files(query_num)
        query_string = query.read()
        query_string = prefix + query_string
        # Replace values
        query_string = query_string.replace("{topic_uri}", topic_uri)
        print("Query 5\n" + query_string)
        results = Graph()
        results = graph.query(query_string)
        save_results(results, output)


class Q6:
    # 6. For a student, list all topics (no duplicates) that this student is familiar with
    # (based on the completed courses for this student that are better than an \F" grade)
    @staticmethod
    def query(student_id, prefix, graph):
        query_num = "q6"
        query, output = open_query_files(query_num)
        query_string = query.read()
        query_string = prefix + query_string
        # Replace values

        print("Query 6\n" + query_string)
        results = Graph()
        results = graph.query(query_string)
        save_results(results, output)


def open_query_files(query_num):
    make_sure_path_exists("./output/")

    query_file_path = "./sparql_queries/" + f"{query_num}.txt"
    output_file_path = "./output/" + f"{query_num}_response.txt"

    query = open(query_file_path, "r")
    output = open(output_file_path, "w+")

    return query, output


def save_results(results, output_file):
    for row in results:
        result = ''
        for entry in row:
            result = result + str(entry) + ' '
        result = result + '\n'
        print(result)
        output_file.write(str(result))


# Source: https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory/14364249#14364249
# And https://github.com/melanie-t/COMP472_Project1_W20/blob/master/src/helper_functions.py
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
# End source
