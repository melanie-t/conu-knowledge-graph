from json import JSONDecodeError

import requests
import urllib.parse
import json
from src.courseExtraction.CourseExtractorFromTxt import CourseExtractorFromTxt


class SpotlightAssociations:

    # there is also the @confidence that could be taken
    @staticmethod
    def get_keywords_from_text(text):
        url_encoded_text = urllib.parse.quote_plus(text)
        url = "https://api.dbpedia-spotlight.org/en/annotate?text="+url_encoded_text
        response_details = requests.get(url, headers={"Accept":"application/json"})
        parsed_response = json.loads(response_details.content)

        term_link_array = [[0 for j in range(2)] for i in range(len(parsed_response['Resources']))]
        for i in range(len(parsed_response['Resources'])):
            term_link_array[i][0] = parsed_response['Resources'][i]['@surfaceForm'] # term
            term_link_array[i][1] = parsed_response['Resources'][i]['@URI'] # link

        return term_link_array

    @staticmethod
    def __get_keywords_from_text_to_file(text, fileURI):
        url_encoded_text = urllib.parse.quote_plus(text)
        url = "https://api.dbpedia-spotlight.org/en/annotate?text=" + url_encoded_text
        response_details = requests.get(url, headers={"Accept": "application/json"})
        parsed_response = ''
        try:
            parsed_response = json.loads(response_details.content.decode("utf-8"))
        except JSONDecodeError as e:
            print(e)

        if 'Resources' in parsed_response:
            outputfile = open(fileURI,'a')
            for i in range(len(parsed_response['Resources'])):
                outputfile.write('\"'+parsed_response['Resources'][i]['@surfaceForm']+'\" '+parsed_response['Resources'][i]['@URI']+'\n')
            outputfile.close()
            print(str(len(parsed_response['Resources']))+' links added.')
        return

    @staticmethod
    def write_all_keywords_to_file(): # not working: too many requests, spotlight stops answering
        output_file = 'spotlight-keywords.txt'
        open(output_file, 'w').close() # clears the file
        CourseExtractorFromTxt.path_to_courses = '../courseExtraction/courses.txt'
        courses_list = CourseExtractorFromTxt.get_course_list()
        for i in range(len(courses_list)):
            if len(courses_list[i].title)>0:
                SpotlightAssociations.__get_keywords_from_text_to_file(courses_list[i].title,output_file)
            if len(courses_list[i].description)>0:
                SpotlightAssociations.__get_keywords_from_text_to_file(courses_list[i].description,output_file)
            print(i)

        print("Done transferring keywords and their links in "+output_file)
        return

if __name__ == "__main__":
    """text = "Concordia is a university in Montreal."
    term_link_array = SpotlightAssociations.get_keywords_from_text(text)
    for i in range(len(term_link_array)):
        print(term_link_array[i][0])
        print(term_link_array[i][1])"""
    SpotlightAssociations.write_all_keywords_to_file()
