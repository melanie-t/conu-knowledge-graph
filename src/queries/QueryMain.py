from rdflib import Graph

from src.queries.Queries import open_query_files, save_results

if __name__ == '__main__':
    output_file = "../../output.ttl"
    graph = Graph()
    graph.parse(output_file, format="turtle")

    for i in range(1, 7):
        query_num = "q" + str(i)
        query, output_file = open_query_files(query_num)
        query_string = query.read()
        print(f"Query {i}\n" + query_string)
        results = Graph()
        results = graph.query(query_string)
        save_results(results, output_file)

