from rdflib import URIRef, Literal
from rdflib.namespace import RDF, RDFS
from src.spotlightAnnotations import SpotlightAssociations


# Find spotlight associations for specific course URI
def init_topics(graph, course_uri_set):
    topic_namespace_uri = "http://www.example.org/topic/"
    sioc_namespace = "http://rdfs.org/sioc/ns#"

    for course in course_uri_set:
        print(course)
        try:
            termLink = SpotlightAssociations.SpotlightAssociations.get_keywords_from_text(
                course[1] + " " + course[2])

            if len(termLink) != 0:
                for entity in termLink:
                    label = entity[0]
                    uri = entity[1]
                    graph.add((URIRef(course[0]), URIRef(sioc_namespace + "topic"), URIRef(uri)))
                    graph.add((URIRef(uri), RDF.type, URIRef(topic_namespace_uri)))
                    graph.add((URIRef(uri), RDFS.label, Literal(label)))

                    output_file = open("spotlight.txt", 'r')
                    association = (str(course[0]) + " " + str(label) + " " + str(uri))
                    output_file.write(association)
                    print("Saved to file" + association)
                    output_file.close()

        except Exception as e:
            print(e)

    return graph
