from rdflib import URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS


# Generate topics using DBPedia Spotlight, we will use the generated text files to add topic triples
def init_topics(graph):
    sioc_namespace = "http://rdfs.org/sioc/ns#"
    topic_namespace_uri = "http://www.example.org/topic/"

    # Add Topic triples
    all_topics = open("../spotlightAnnotations/spotlight-set.txt").readlines()
    for topic in all_topics:
        topic.replace("\\n", "")
        topic_arg = topic.split("\" ")
        label = topic_arg[0].replace("\"", "")

        uri = topic_arg[1]
        graph.add((URIRef(uri), RDF.type, URIRef(topic_namespace_uri)))
        graph.add((URIRef(uri), RDFS.label, Literal(label)))

    # Adding Topics for Courses
    all_courses = open("../spotlightAnnotations/spotlight-courses.txt").readlines()
    for course in all_courses:
        course.replace("\\n", "")
        # course_arg = course.split(" ")
        # course_uri = course_arg[0]
        # topic_uri = course_arg[2]
        # graph.add((URIRef(course_uri), URIRef(sioc_namespace+'topic'), topic_uri))


# graph = Graph()
# init_topics(graph)
# for row in graph:
#     print(row)
