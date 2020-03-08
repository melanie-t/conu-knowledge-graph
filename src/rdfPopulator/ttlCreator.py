from rdflib import URIRef, Graph, Literal
from rdflib.namespace import RDF, RDFS
from src.courseExtraction.CourseExtractorFromTxt import CourseExtractorFromTxt
from src.studentCreation.StudentGenerator import StudentGenerator
if __name__ == '__main__':
    courses_namespace_uri = "http://www.example.org/course/"
    property_uri = "http://www.example.org/property/"
    student_namespace_uri = "http://www.example.org/student/"
    semester_namespace_uri = "http://www.example.org/semester/"

    schema_namespace_uri = "http://schema.org/"

    dbpedia_page_uri = "http://dbpedia.org/page/"
    dbpedia_property_uri = "http://dbpedia.org/property/"
    dbpedia_ontology_uri = "http://dbpedia.org/ontology/"

    g = Graph()

    # first add the university
    g.add((URIRef(dbpedia_page_uri+"Concordia_University"), URIRef(dbpedia_ontology_uri+"type"), URIRef(dbpedia_page_uri+"Public_university")))
    g.add((URIRef(dbpedia_page_uri+"Concordia_University"), URIRef(dbpedia_property_uri+"uniname"), Literal("Concordia University"))) # name

    print("Parsing")
    # get the courses
    CourseExtractorFromTxt.path_to_courses = '../courseExtraction/courses.txt'
    courses_list = CourseExtractorFromTxt.get_course_list()

    # create a level for categories (acronyms, so COMP, SOEN, ...)
    # then create a deeper level for identification (number of class)
    # when in that deeper level, each node will have a title and a description
    observed_acronym = ''
    """
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
            i+=1
    """
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

        g.serialize(destination='output.ttl', format='turtle')