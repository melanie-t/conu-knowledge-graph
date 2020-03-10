import re

from rdflib import URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS


# Generate topics using DBPedia Spotlight, we will use the generated text files to add topic triples
def init_topics(graph):
    sioc_namespace = "http://rdfs.org/sioc/ns#"
    topic_namespace_uri = "http://www.example.org/topic/"
    courses_namespace_uri = "http://www.example.org/course/"

    # Add Topic triples
    all_topics = open("../spotlightAnnotations/spotlight-set.txt").readlines()
    for topic in all_topics:
        topic = topic.replace("\n", "")
        topic_arg = topic.split("\" ")
        label = topic_arg[0].replace("\"", "")

        uri = topic_arg[1]
        graph.add((URIRef(uri), RDF.type, URIRef(topic_namespace_uri)))
        graph.add((URIRef(uri), RDFS.label, Literal(label.title())))

    # Adding Topics for Courses

    all_courses = open("../spotlightAnnotations/spotlight-linkCourse.txt").readlines()
    for course in all_courses:
        course = course.replace("\n", "")
        course_arg = re.split('\" | \[', course)
        topic_uri = course_arg[1]
        course_uris = course_arg[2]
        course_uris = course_uris.replace("]", "")
        course_list = course_uris.split(",")

        for course_uri in course_list:
            if course_uri != '':
                graph.add((URIRef(courses_namespace_uri+course_uri), URIRef(sioc_namespace + 'topic'), URIRef(topic_uri)))