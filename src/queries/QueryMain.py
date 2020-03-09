from rdflib import Graph
from src.queries import Queries
from src.queries.old_queries import create_prefix

if __name__ == '__main__':
    output_file = "../rdfPopulator/output.ttl"
    g = Graph()
    g.parse(output_file, format="turtle")
    prefix = create_prefix(output_file)

    # queries.Q1.query(prefix=prefix, graph=g)
    # queries.Q3.query(course_uri="http://www.example.org/course/ELEC/423", prefix=prefix, graph=g)
    Queries.Q4.query(student_id="333333", prefix=prefix, graph=g)