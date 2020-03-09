from pyparsing import ParseException
from rdflib import URIRef, Graph, Literal
from rdflib.namespace import RDF, RDFS, Namespace, NamespaceManager
from src.spotlightAnnotations import SpotlightAssociations
prefix = ''

# Import prefixes from ttl
try:
    # Source: https://stackabuse.com/read-a-file-line-by-line-in-python/
    filepath = '../rdfPopulator/output.ttl'
    with open(filepath) as f:
        line = f.readline()
        prefix = prefix + line
        cnt = 1
        while line:
            line = f.readline()
            if line in ['\n', '\r\n']:
                break
            prefix = prefix + line
            cnt += 1
finally:
    f.close()

prefix = prefix.replace("@prefix", "PREFIX")
prefix = prefix.replace(" .", "")

# Prefixes added for simplifying queries
prefix = prefix

g = Graph()
g.parse("../rdfPopulator/output.ttl", format="turtle")

# Defining namespaces
sioc_namespace = "http://rdfs.org/sioc/ns#"
topic_namespace_uri = "http://www.example.org/topic/"
courses_namespace_uri = "http://www.example.org/course/"

# Find spotlight associations for specific course URI
course_uri = "http://www.example.org/course/ACCO/220"
course_description = "This course provides an introduction to accounting principles underlying the preparation of financial reports with an emphasis on the relationship between accounting information and production decisions. It examines the relationship between costs, production volume, and profit, as well as the practical benefits of standard costs for planning and control purposes. The role of accounting information in various manufacturing decisions is also highlighted."
course_title = "Financial and Managerial Accounting"

termLink = []
termLink = SpotlightAssociations.SpotlightAssociations.get_keywords_from_text(course_title + " " + course_description)


for entity in termLink:
    label = entity[0]
    uri = entity[1]
    g.add((URIRef(course_uri), URIRef(sioc_namespace+"topic"), URIRef(uri)))
    g.add((URIRef(uri), RDF.type, URIRef(topic_namespace_uri)))
    g.add((URIRef(uri), RDFS.label, Literal(label)))

course_uri = "http://www.example.org/course/ACCO/220"
query = prefix + """
SELECT ?label ?topic
WHERE {
<http://www.example.org/course/ACCO/220> sioc:topic ?topic .
?topic rdfs:label ?label .
}
"""
print(query)
res4 = g.query(query)

for row in res4:
    print(row['label'], row['topic'])

