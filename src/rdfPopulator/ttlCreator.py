from rdflib import URIRef, Graph, Literal
from rdflib.namespace import RDF, RDFS, Namespace, NamespaceManager
from src.courseExtraction.CourseExtractorFromTxt import CourseExtractorFromTxt
from src.studentCreation.StudentGenerator import StudentGenerator
from src.spotlightAnnotations import SpotlightAssociations

if __name__ == '__main__':
    courses_namespace_uri = "http://www.example.org/course/"
    property_uri = "http://www.example.org/property/"
    student_namespace_uri = "http://www.example.org/student/"
    semester_namespace_uri = "http://www.example.org/semester/"
    topic_namespace_uri = "http://www.example.org/topic/"

    schema_namespace_uri = "http://schema.org/"

    dbpedia_page_uri = "http://dbpedia.org/page/"
    dbpedia_property_uri = "http://dbpedia.org/property/"
    dbpedia_ontology_uri = "http://dbpedia.org/ontology/"

    sioc_namespace = "http://rdfs.org/sioc/ns#"

    g = Graph()

    course_uri_set = set()

    # Add Topic Class definition
    g.add((URIRef(topic_namespace_uri), RDF.type, RDFS.Class))
    g.add((URIRef(topic_namespace_uri), RDFS.subClassOf, URIRef(courses_namespace_uri)))

    # first add the university
    g.add((URIRef(dbpedia_page_uri+"Concordia_University"), URIRef(dbpedia_ontology_uri+"type"), URIRef(dbpedia_page_uri+"Public_university")))
    g.add((URIRef(dbpedia_page_uri+"Concordia_University"), URIRef(dbpedia_property_uri+"uniname"), Literal("Concordia University"))) # name

    print("Parsing")
    # get the courses
    CourseExtractorFromTxt.path_to_courses = '../courseExtraction/courses.txt'
    courses_list = CourseExtractorFromTxt.get_course_list()
    # Prefix creation
    # from https://stackoverflow.com/questions/55182311/parsing-turtle-with-python-rdflib-cant-specify-iri-prefix
    g.namespace_manager.bind('sch', schema_namespace_uri)
    g.namespace_manager.bind('exprop', property_uri)
    g.namespace_manager.bind('dbp', dbpedia_property_uri)
    g.namespace_manager.bind('dbo', dbpedia_ontology_uri)
    g.namespace_manager.bind('course', courses_namespace_uri)
    g.namespace_manager.bind('student', student_namespace_uri)
    g.namespace_manager.bind('topic', topic_namespace_uri)
    g.namespace_manager.bind('sioc', sioc_namespace)

    # first add the university
    g.add((URIRef(dbpedia_page_uri+"Concordia_University"), URIRef(dbpedia_ontology_uri+"type"), URIRef(dbpedia_page_uri+"Public_university")))
    g.add((URIRef(dbpedia_page_uri+"Concordia_University"), URIRef(dbpedia_property_uri+"uniname"), Literal("Concordia University"))) # name

    # create a level for categories (acronyms, so COMP, SOEN, ...)
    # then create a deeper level for identification (number of class)
    # when in that deeper level, each node will have a title and a description
    observed_acronym = ''
    i = 0
    for i in range(len(courses_list)):
        if len(observed_acronym) == 0:
            observed_acronym = courses_list[i].subject
        elif observed_acronym != courses_list[i].subject:
            observed_acronym = courses_list[i].subject

        uri_to_acronym = URIRef(courses_namespace_uri+observed_acronym)
        g.add((uri_to_acronym, RDF.type, URIRef(courses_namespace_uri+'CourseAcronym')))
        g.add((uri_to_acronym, URIRef(property_uri+"offered_at"), URIRef(dbpedia_page_uri+"Concordia_University")))

        while i < len(courses_list) and observed_acronym == courses_list[i].subject:
            # use acronym (COMP) and number (108) in url to give context to know where to search for
            uri_to_number = URIRef(courses_namespace_uri+observed_acronym+'/'+str(courses_list[i].number))
            g.add((uri_to_number, RDFS.subClassOf, uri_to_acronym))
            g.add((uri_to_number, RDF.type, URIRef(courses_namespace_uri+'Course')))
            g.add((uri_to_number, RDFS.label, Literal(courses_list[i].description))) # set description as label
            g.add((uri_to_number, URIRef(schema_namespace_uri+'name'), Literal(courses_list[i].title))) # set title as name
            course_uri_set.add((str(uri_to_number), str(courses_list[i].title), str(courses_list[i].description)))
            i += 1

    # now add the students
    StudentGenerator.generate_students_classes()
    students = StudentGenerator.generate_students_classes()

    for i in range(len(students)):
        g.add((URIRef(student_namespace_uri+students[i].email), URIRef(schema_namespace_uri+'name'), Literal(students[i].name)))
        g.add((URIRef(student_namespace_uri+students[i].email), URIRef(property_uri+"identified_by"), Literal(students[i].id)))
        g.add((URIRef(student_namespace_uri+students[i].email), RDF.type, URIRef(student_namespace_uri+"Student")))

        for j in range(len(students[i].curriculum)):
            course_uri = courses_namespace_uri+students[i].curriculum[j].subject+'/'+str(students[i].curriculum[j].number)
            # used year with semester because student cannot do the same course twice in a single semester
            student_course_registration_uri = course_uri+'/'+students[i].email+'/'+students[i].curriculum[j].getTermSemester()\
                                              +'/'+students[i].curriculum[j].term.year
            # student enrolled to class
            g.add((URIRef(student_namespace_uri+students[i].email), URIRef(property_uri+"enrolled_to"),
                   URIRef(course_uri)))
            # student enrolled in 'date'
            g.add((URIRef(student_namespace_uri+students[i].email), URIRef(property_uri+"enrolled_in"),
                   URIRef(student_course_registration_uri)))
            # student enrolled year 'year'
            g.add((URIRef(student_course_registration_uri), URIRef(property_uri+"enrolled_year"),
                   Literal(students[i].curriculum[j].term.year)))
            # student enrolled semester 'season'
            g.add((URIRef(student_course_registration_uri), URIRef(property_uri + "enrolled_semester"),
                   URIRef(semester_namespace_uri+students[i].curriculum[j].getTermSemester())))
            # student completed with 'grade'
            g.add((URIRef(student_course_registration_uri), URIRef(property_uri+"completed_with"),
                   Literal(students[i].curriculum[j].grade)))
            # 'season' is a TermSeason
            g.add((URIRef(semester_namespace_uri+students[i].curriculum[j].getTermSemester()), RDF.type,
                   URIRef(semester_namespace_uri+"TermSeason")))

    # Find spotlight associations for specific course URI
    for course in course_uri_set:
        print(course)
        termLink = []
        try:
            termLink = SpotlightAssociations.SpotlightAssociations.get_keywords_from_text(
                course[1] + " " + course[2])

            if len(termLink) != 0:
                for entity in termLink:
                    label = entity[0]
                    uri = entity[1]
                    g.add((URIRef(course[0]), URIRef(sioc_namespace + "topic"), URIRef(uri)))
                    g.add((URIRef(uri), RDF.type, URIRef(topic_namespace_uri)))
                    g.add((URIRef(uri), RDFS.label, Literal(label)))

                    outputfile = open("spotlight.txt", 'a')
                    outputfile.write(URIRef(course[0], label, uri))
                    outputfile.close()

        except Exception as e:
            print(e)

        g.serialize(destination='output.ttl', format='turtle')
