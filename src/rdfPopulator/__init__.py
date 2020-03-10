from rdflib import Graph
from src.rdfPopulator.NamespacePopulator import init_namespace
from src.rdfPopulator.StudentPopulator import init_student
from src.rdfPopulator.CoursePopulator import init_courses
from src.rdfPopulator.TopicsPopulator import init_topics

# Create the RDF schema in Turtle Format
if __name__ == '__main__':
    graph = Graph()
    # 1. Initialize namespace and add university
    init_namespace(graph)

    # 2. Add students to graph
    init_student(graph)

    # 3. Add courses to graph
    course_set = set()
    init_courses(graph, course_set)

    # 4. Generate topics using course set
    # Takes the longest to get topics
    init_topics(graph)

    graph.serialize(destination='output.ttl', format='turtle')
