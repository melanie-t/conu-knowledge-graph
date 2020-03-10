from rdflib import URIRef, Literal
from rdflib.namespace import RDF, RDFS


def init_namespace(graph):
    courses_namespace_uri = "http://www.example.org/course/"
    property_uri = "http://www.example.org/property/"
    student_namespace_uri = "http://www.example.org/student/"
    topic_namespace_uri = "http://www.example.org/topic/"

    schema_namespace_uri = "http://schema.org/"

    dbpedia_page_uri = "http://dbpedia.org/page/"
    dbpedia_property_uri = "http://dbpedia.org/property/"
    dbpedia_ontology_uri = "http://dbpedia.org/ontology/"

    sioc_namespace = "http://rdfs.org/sioc/ns#"

    # Add Topic Class definition
    graph.add((URIRef(topic_namespace_uri), RDF.type, RDFS.Class))
    graph.add((URIRef(topic_namespace_uri), RDFS.subClassOf, URIRef(courses_namespace_uri)))

    # Add the University Class definition
    graph.add((URIRef(dbpedia_page_uri + "Concordia_University"), URIRef(dbpedia_ontology_uri + "type"), URIRef(dbpedia_page_uri + "Public_university")))
    graph.add((URIRef(dbpedia_page_uri + "Concordia_University"), URIRef(dbpedia_property_uri + "uniname"), Literal("Concordia University"))) # name

    # Namespace prefix creation
    # from https://stackoverflow.com/questions/55182311/parsing-turtle-with-python-rdflib-cant-specify-iri-prefix
    graph.namespace_manager.bind('sch', schema_namespace_uri)
    graph.namespace_manager.bind('exprop', property_uri)
    graph.namespace_manager.bind('dbp', dbpedia_property_uri)
    graph.namespace_manager.bind('dbo', dbpedia_ontology_uri)
    graph.namespace_manager.bind('course', courses_namespace_uri)
    graph.namespace_manager.bind('student', student_namespace_uri)
    graph.namespace_manager.bind('topic', topic_namespace_uri)
    graph.namespace_manager.bind('sioc', sioc_namespace)

    return graph
