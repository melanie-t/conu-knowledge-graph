from pyparsing import ParseException
import textwrap

from termcolor import colored
from src.chatbot.InputParser import parseInput
from rdflib import Graph


def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))


def main():
    g = Graph()
    conu_schema = "../output.ttl"
    g.parse(conu_schema, format="turtle")
    print(colored("Hi there, I am ConU ChatBot :)", 'red'))
    print(colored("Sample Questions\n"
                  "\t What's COMP 474 about?\n"
                  "\t Which courses did Bianca Patry take?\n"
                  "\t Which courses cover Natural Language Processing?\n"
                  "\t Who is familiar with Education?\n", 'yellow'))
    while True:
        # q1 = "What's COMP 474 about?"
        # q2 = "Which courses did Bianca Patry take?"
        # q3 = "Which courses cover Natural Language Processing?"
        # q4 = "Who is familiar with Education?"

        questionInput = input(colored("What would you like to know? ", 'red'))

        try:
            queryOutput = parseInput(questionInput)
            query = queryOutput.query
            message = queryOutput.message
        except:
            print("I am unable to answer your question at the moment. Please try another question.\n")
            continue

        results = Graph()
        results = g.query(query)
        print(colored(message, 'red'))
        if (queryOutput.printQueryWithTable(results) == False):
            i = 1
            for row in results:
                result = ''
                for entry in row:
                    result = result + str(entry) + ' '
                result = result + '\n'
                stringRes = result
                print(str(i), ': ', wrap(stringRes, 120), '\n')
                i = i + 1


if __name__ == "__main__":
    main()
