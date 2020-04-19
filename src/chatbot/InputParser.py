import spacy
from src.chatbot.QueryCreator import query1_courseDescription, query2_studentCourses, query3_courseTopics, query4_studentsFamiliar


def parseInput(questionInput):
    nlp = spacy.load("en_core_web_sm")

    tokenList = []
    lemmaList = []
    posList = []
    tagList = []

    question = nlp(questionInput)
    for token in question:
        tokenList.append(token.text)
        lemmaList.append(token.lemma_)
        posList.append(token.pos_)
        tagList.append(token.tag_)

    query = ''

    # Q1
    if 'be' in lemmaList and 'about' in lemmaList:
        # print("Query 1")
        for i, pos in enumerate(posList):
            if pos == 'PROPN' and posList[i+1] == 'NUM':
                query = query1_courseDescription(subject=tokenList[i], code=tokenList[i+1])

    # Q2
    elif 'do' in lemmaList and 'course' in lemmaList and 'take' in lemmaList:
        # print("Query 2")
        student = ''
        for i, pos in enumerate(posList):
            if pos == 'PROPN' and posList[i+1] == 'PROPN':      # First and last name
                student = tokenList[i] + " " + tokenList[i+1]
            elif tagList[i] == 'ADD':       # Email
                student = tokenList[i]
            elif pos == 'NUM':      # Student ID
                student = tokenList[i]
        query = query2_studentCourses(student.strip())

    # Q3
    elif 'course' in lemmaList and 'cover' in lemmaList:
        # print("Query 3")
        topic = ''
        for i, pos in enumerate(posList):
            if pos == 'PROPN':
                topic = topic + tokenList[i] + " "
        query = query3_courseTopics(topic.strip())

    # Q4
    elif 'who' in lemmaList and 'be' in lemmaList and 'familiar' in lemmaList:
        # print("Query 4")
        topic = ''
        for i, pos in enumerate(posList):
            if pos == 'PROPN':
                topic = topic + tokenList[i] + " "
        query = query4_studentsFamiliar(topic.strip())

    else:
        raise

    return query
