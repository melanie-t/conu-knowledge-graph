from rdflib import URIRef, Literal
from rdflib.namespace import RDF, RDFS

from src.courseExtraction import CourseLinks
from src.courseExtraction.CourseExtractorFromTxt import CourseExtractorFromTxt

# create a level for categories (acronyms, so COMP, SOEN, ...)
# then create a deeper level for identification (number of class)
# when in that deeper level, each node will have a title and a description
def init_courses(graph, course_uri_set):
    courses_namespace_uri = "http://www.example.org/course/"
    property_uri = "http://www.example.org/property/"
    schema_namespace_uri = "http://schema.org/"
    dbpedia_page_uri = "http://dbpedia.org/page/"
    sioc_namespace = "http://rdfs.org/sioc/ns#"

    print("Parsing")
    # get the courses
    CourseExtractorFromTxt.path_to_courses = '../courseExtraction/courses.txt'
    courses_list = CourseExtractorFromTxt.get_course_list()

    observed_acronym = ''
    i = 0
    for i in range(len(courses_list)):
        if len(observed_acronym) == 0:
            observed_acronym = courses_list[i].subject
        elif observed_acronym != courses_list[i].subject:
            observed_acronym = courses_list[i].subject

        uri_to_acronym = URIRef(courses_namespace_uri + observed_acronym)
        graph.add((uri_to_acronym, RDF.type, URIRef(courses_namespace_uri + 'CourseAcronym')))
        graph.add((uri_to_acronym, URIRef(property_uri + "offered_at"), URIRef(dbpedia_page_uri + "Concordia_University")))

        while i < len(courses_list) and observed_acronym == courses_list[i].subject:
            # use acronym (COMP) and number (108) in url to give context to know where to search for
            uri_to_number = URIRef(courses_namespace_uri + observed_acronym + '/' + str(courses_list[i].number))
            course_ref_link = CourseLinks.CourseLinks.getUrlForCourseAcronym(observed_acronym)
            graph.add((uri_to_number, RDFS.subClassOf, uri_to_acronym))
            graph.add((uri_to_number, RDF.type, URIRef(courses_namespace_uri + 'Course')))
            graph.add((uri_to_number, RDFS.label, Literal(observed_acronym + " " + courses_list[i].number + " : " + courses_list[i].title)))
            graph.add((uri_to_number, URIRef(sioc_namespace+"about"), Literal(courses_list[i].description)))  # set description as sioc:about
            graph.add((uri_to_number, RDFS.seeAlso, URIRef(course_ref_link))) # rdfs:seeAlso link to Concordia's reference page
            graph.add(
                (uri_to_number, URIRef(schema_namespace_uri + 'name'), Literal(courses_list[i].title)))  # set title as name
            course_uri_set.add((str(uri_to_number), str(courses_list[i].title), str(courses_list[i].description)))
            i += 1

    return graph