prefix = "PREFIX course: <http://www.example.org/course/> " \
         "PREFIX dbo: <http://dbpedia.org/ontology/> " \
         "PREFIX dbp: <http://dbpedia.org/property/> " \
         "PREFIX exprop: <http://www.example.org/property/>" \
         "PREFIX ns1: <http://xmlns.com/foaf/0.1/> " \
         "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " \
         "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> " \
         "PREFIX sch: <http://schema.org/> " \
         "PREFIX sioc: <http://rdfs.org/sioc/ns#> " \
         "PREFIX student: <http://www.example.org/student/> " \
         "PREFIX topic: <http://www.example.org/topic/> " \
         "PREFIX xml: <http://www.w3.org/XML/1998/namespace> " \
         "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> " \
         "PREFIX foaf: <http://xmlns.com/foaf/0.1/>"


def query1_courseDescription(subject, code):
    query = prefix + \
           f"SELECT ?course_description " \
           f"WHERE {{ "\
           f"           ?course 	rdf:type 		course:Course ; " \
           f"          	            course:code 	\"{code}\" ; " \
           f"          	            course:subject 	\"{subject}\" ; " \
           f"          	            sioc:about 		?course_description . " \
           f"}}"
    # print(query)
    return query


def query2_studentCourses(student):
    query = prefix + \
            f"SELECT ?courseName ?grade ?term ?year " \
            f"WHERE {{" \
            f"          ?student 		    sch:name|" \
            f"							    foaf:mail|" \
            f"							    exprop:identified_by		\"{student}\" ; " \
            f"				 			    exprop:enrolled_in          ?course_enrolled . " \
            f"  		?course_enrolled 	course: 					?course ; " \
            f"                   			exprop:completed_with 		?grade ; " \
            f"                   			exprop:enrolled_semester 	?term ; " \
            f"                   			exprop:enrolled_year 		?year . " \
            f"  		?course 			rdfs:label 					?courseName ." \
            f"}}"
    # print(query)
    return query


def query3_courseTopics(topic):
    query = prefix + \
            f"SELECT ?courseName ?courseDescription " \
            f"WHERE {{  " \
            f"          ?topic 	            rdf:type 		topic: ;" \
            f"  			                rdfs:label 		\"{topic}\" ." \
            f"          ?course 	        rdf:type 		course:Course ;" \
            f"		  	                    rdfs:label 		?courseName ;" \
            f"		  	                    sioc:topic 		?topic ." \
            f"          OPTIONAL {{?course sioc:about ?courseDescription }}" \
            f"}}"
    # print(query)
    return query


def query4_studentsFamiliar(topic):
    query = prefix + \
            f"SELECT ?studentName ?studentId ?studentEmail " \
            f"WHERE {{" \
            f"          ?topic              rdfs:label              \"{topic}\" ." \
            f"          ?course             sioc:topic              ?topic ." \
            f"          ?student            exprop:enrolled_in      ?course_enrolled ;" \
            f"                              sch:name                ?studentName ;" \
            f"                              foaf:mail               ?studentEmail ;" \
            f"                              exprop:identified_by    ?studentId ." \
            f"          ?course_enrolled    course:                 ?course ;" \
            f"                              exprop:completed_with ?grade ." \
            f"          FILTER (?grade >= 50)" \
            f"}}"
    # print(query)
    return query


# query1_courseDescription(subject="COMP", code="474")
# query2_studentCourses("Bianca Patry")
# query3_courseTopics("Natural Language Processing")
# query4_studentsFamiliar("Education")
