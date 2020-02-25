import spotlight


def get_topics(text):
    host = "https://api.dbpedia-spotlight.org/en/annotate"
    confidence = 0.40
    support = 20

    topics_list = []
    annotations = spotlight.annotate(host, text, confidence, support)

    for prop in annotations:
        topics_list.append(prop['URI'])

    return topics_list


# Example
courseDescription = "Prerequisite: COMP 346. Principles of distributed computing: scalability, transparency, concurrency, consistency, fault tolerance, high availability. " \
                    "Clientserver interaction technologies: interprocess communication, sockets, group communication, remote procedure call, remote method invocation, object request broker, CORBA, web services. " \
                    "Server design techniques: process replication, fault tolerance through passive replication, high availability through active replication, coordination and agreement, transactions and concurrency control. " \
                    "Lectures: three hours per week. " \
                    "Tutorial one hour per week. Laboratory: two hours per week."
topics = get_topics(courseDescription)
print(topics)
