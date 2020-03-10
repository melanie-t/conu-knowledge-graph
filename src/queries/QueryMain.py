from rdflib import Graph
from src.queries import Queries

def create_prefix(output_file_path):
    prefix_list = ''
    # Import prefixes from ttl
    try:
        # Source: https://stackabuse.com/read-a-file-line-by-line-in-python/
        filepath = '../rdfPopulator/output.ttl'
        with open(filepath) as f:
            line = f.readline()
            prefix_list = prefix_list + line
            cnt = 1
            while line:
                line = f.readline()
                if line in ['\n', '\r\n']:
                    break
                prefix_list = prefix_list + line
                cnt += 1
    finally:
        f.close()

    prefix_list = prefix_list.replace("@prefix", "PREFIX")
    prefix_list = prefix_list.replace(" .", "")

    return prefix_list


if __name__ == '__main__':
    output_file = "../rdfPopulator/output.ttl"
    g = Graph()
    g.parse(output_file, format="turtle")
    prefix = create_prefix(output_file)

    # Queries.Q1.query(prefix=prefix, graph=g)
    # Queries.Q2.query(prefix=prefix, graph=g)
    # Queries.Q3.query(course_uri="http://www.example.org/course/COMM/223", prefix=prefix, graph=g)
    # Queries.Q4.query(student_id="333333", prefix=prefix, graph=g)
    Queries.Q5.query(topic_uri="http://dbpedia.org/resource/Superconductivity", prefix=prefix, graph=g)
    # Queries.Q6.query(student_id="333333", prefix=prefix, graph=g)