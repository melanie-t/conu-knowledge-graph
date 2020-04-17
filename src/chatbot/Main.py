from src.chatbot.inputParser import parseInput
from rdflib import Graph


def main():
    g = Graph()
    output_file = "../rdfPopulator/output.ttl"
    g.parse(output_file, format="turtle")
    print("Hi there, I am ConU ChatBot :)")
    while True:

        q1 = "What's COMP 474 about?"
        q2 = "Which courses did Bianca Patry take?"
        q3 = "Which courses cover Natural Language Processing?"
        q4 = "Who is familiar with Education?"

        questionInput = input("What would you like to know? ")
        #questionInput = q1
        query = parseInput(questionInput)
        print(query)
        results = Graph()
        results = g.query(query)
        #print(results)
        i = 1
        for row in results:
            result = ''
            for entry in row:
                result = result + str(entry) + ' '
            result = result + '\n'
            print(i , ":", result)
            i = i + 1


if __name__ == "__main__":
    main()


