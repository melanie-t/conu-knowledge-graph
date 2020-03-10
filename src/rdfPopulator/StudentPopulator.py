from rdflib import URIRef, Literal, Graph
from rdflib.namespace import RDF, FOAF
from src.studentCreation.StudentGenerator import StudentGenerator


def init_student(graph):
    student_namespace_uri = "http://www.example.org/student/"
    courses_namespace_uri = "http://www.example.org/course/"
    property_uri = "http://www.example.org/property/"
    schema_namespace_uri = "http://schema.org/"
    semester_namespace_uri = "http://www.example.org/semester/"

    StudentGenerator.generate_students_classes()
    students = StudentGenerator.generate_students_classes()

    for i in range(len(students)):
        graph.add((URIRef(student_namespace_uri + students[i].email), URIRef(schema_namespace_uri + 'name'),
                   Literal(students[i].name)))
        graph.add((URIRef(student_namespace_uri + students[i].email), URIRef(property_uri + "identified_by"),
                   Literal(students[i].id)))
        graph.add((URIRef(student_namespace_uri + students[i].email), RDF.type, URIRef(student_namespace_uri + "Student")))
        graph.add((URIRef(student_namespace_uri + students[i].email), FOAF.mail, Literal(students[i].email)))

        for j in range(len(students[i].curriculum)):
            course_uri = courses_namespace_uri + students[i].curriculum[j].subject + '/' + str(
                students[i].curriculum[j].number)
            # used year with semester because student cannot do the same course twice in a single semester
            student_course_registration_uri = course_uri + '/' + students[i].email + '/' + students[i].curriculum[
                j].getTermSemester() \
                                              + '/' + students[i].curriculum[j].term.year
            # student enrolled to class
            graph.add((URIRef(student_namespace_uri + students[i].email), URIRef(property_uri + "enrolled_to"),
                       URIRef(course_uri)))
            # student enrolled in 'date'
            graph.add((URIRef(student_namespace_uri + students[i].email), URIRef(property_uri + "enrolled_in"),
                       URIRef(student_course_registration_uri)))
            # student enrolled year 'year'
            graph.add((URIRef(student_course_registration_uri), URIRef(property_uri + "enrolled_year"),
                       Literal(students[i].curriculum[j].term.year)))
            # student enrolled semester 'season'
            graph.add((URIRef(student_course_registration_uri), URIRef(property_uri + "enrolled_semester"),
                       URIRef(semester_namespace_uri + students[i].curriculum[j].getTermSemester())))
            # student completed with 'grade'
            graph.add((URIRef(student_course_registration_uri), URIRef(property_uri + "completed_with"),
                       Literal(students[i].curriculum[j].grade)))
            # course name
            graph.add((URIRef(student_course_registration_uri), URIRef(courses_namespace_uri), URIRef(course_uri)))
            # 'season' is a TermSeason
            graph.add((URIRef(semester_namespace_uri + students[i].curriculum[j].getTermSemester()), RDF.type,
                       URIRef(semester_namespace_uri + "TermSeason")))

    return graph

g = Graph()
init_student(g)
g.serialize("students.ttl", format="turtle")