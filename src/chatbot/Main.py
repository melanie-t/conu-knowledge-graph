from src.chatbot.inputParser import parseInput


def main():
    print("Hi there, I am ConU ChatBot :)")
    while True:

        q1 = "What's COMP 474 about?"
        q2 = "Which courses did Bianca Patry take?"
        q3 = "Which courses cover Natural Language Processing?"
        q4 = "Who is familiar with Education?"

        questionInput = input("What would you like to know? ")
        query = parseInput(questionInput)
        print(query)


if __name__ == "__main__":
    main()


