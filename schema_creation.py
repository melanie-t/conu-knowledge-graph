from rdflib.namespace import RDFS, RDF, XSD, FOAF
from rdflib import Namespace
from rdflib import URIRef, BNode, Literal
from rdflib import Graph


# Initialize schema classes
def init_schema():
    print("Load schema classes")
    graph = Graph()
    graph.parse("./resources/schema.ttl", format="turtle")
    for s, p, o in graph:
        print(s, p, o)


init_schema()
