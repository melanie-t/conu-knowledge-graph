import re
from src.courseExtraction.Course import Course

"""
This script extracts analyzes a single HTML file and searches for courses in it.
"""

class CourseDataParser:
    acronym_currently_looked = ""  # acronyms disappear after some time because courses are ordered by categories
    index_currently_looked = -1
    acronyms_searched_for_CDP = None # copy of the list for the class' use
    is_not_set = 0

    @staticmethod
    def __smallerThanArrayAndNotEmptyOrStartingWithWhiteSpace(x, whitespaceless_title):
        return x < len(whitespaceless_title) - 1 and (
                    len(whitespaceless_title[x]) == 0 or whitespaceless_title[x].startswith("&"))

    @staticmethod
    def __removeWhiteSpaceFromTitle(html_tagless_string):
        no_results = 1
        index_after_empty_string = 1
        whitespaceless_title = re.split("((&nbsp;)+\s*)+", html_tagless_string[2])
        if len(whitespaceless_title) > no_results:
            x = index_after_empty_string
            while CourseDataParser.__smallerThanArrayAndNotEmptyOrStartingWithWhiteSpace(x, whitespaceless_title):
                x += 1
            return whitespaceless_title[x]
        else:
            return html_tagless_string[2]

    @staticmethod
    def __analyzeCourseSubject(courseSubjectLine):
        tagless_string_division = re.split("<.{1,2}>\s*", courseSubjectLine)
        subject_number = tagless_string_division[1].split(" ") # separating domain (COMP) from number
        subject_number_title = [0 for i in range(3)]
        subject_number_title[0] = subject_number[0]
        if len(subject_number)>=2:
            subject_number_title[1] = re.split("&nbsp;",subject_number[1])[0] # removing extra whitespace

        is_not_only_containing_spaces = not tagless_string_division[2].endswith("&nbsp;")
        backup_index = 4
        primary_index = 2
        if is_not_only_containing_spaces:
            subject_number_title[primary_index] = CourseDataParser.__removeWhiteSpaceFromTitle(tagless_string_division)
        elif len(tagless_string_division)>=5:
            subject_number_title[primary_index] = tagless_string_division[backup_index]
        return subject_number_title

    @staticmethod
    def __analyzeCourseDescription(courseDescriptionLine):
        tagless_string_division = re.split("<.{1,2}>", courseDescriptionLine)
        return tagless_string_division[0]

    @staticmethod
    def __removeIndexFromAcronymsSearched(index):
        if index > CourseDataParser.index_currently_looked: # in that case, index displaced by deletion
            del CourseDataParser.acronyms_searched_for_CDP[CourseDataParser.index_currently_looked]
            CourseDataParser.index_currently_looked = index - 1
        elif index < CourseDataParser.index_currently_looked:
            del CourseDataParser.acronyms_searched_for_CDP[CourseDataParser.index_currently_looked]
            CourseDataParser.index_currently_looked = index

    @staticmethod
    def __removeIndexAndModifyAcronymLooked(index):
        if len(CourseDataParser.acronym_currently_looked) == CourseDataParser.is_not_set:
            CourseDataParser.acronym_currently_looked = CourseDataParser.acronyms_searched_for_CDP[index]
            CourseDataParser.index_currently_looked = index
        elif CourseDataParser.acronym_currently_looked != CourseDataParser.acronyms_searched_for_CDP[index]:
            CourseDataParser.acronym_currently_looked = CourseDataParser.acronyms_searched_for_CDP[index]
            CourseDataParser.__removeIndexFromAcronymsSearched(index)

    @staticmethod
    def extractCoursesFromFile(pathToFile, acronymsSearchedFor):
        """

        :param pathToFile: string that represents the path to the file
        :param acronymsSearchedFor: list of acronyms (COMP, ACCO, etc.) representing classes.
        :return: list of courses
        """
        file = open(pathToFile,'r', encoding="latin-1")
        file_contents = file.readlines()
        file.close()

        course_list = []

        CourseDataParser.acronyms_searched_for_CDP = acronymsSearchedFor.copy()
        CourseDataParser.index_currently_looked = -1
        CourseDataParser.acronym_currently_looked = ""

        skipNextLine = 1
        for i in range(len(file_contents)):
            if file_contents[i].startswith("<b>"):
                for j in range(len(CourseDataParser.acronyms_searched_for_CDP)):
                    if re.search("^<b>\s*"+CourseDataParser.acronyms_searched_for_CDP[j], file_contents[i]):
                        CourseDataParser.__removeIndexAndModifyAcronymLooked(j)
                        subject_number_title = CourseDataParser.__analyzeCourseSubject(file_contents[i])
                        description = CourseDataParser.__analyzeCourseDescription(file_contents[i+1])
                        course_list.append(Course(subject_number_title[1], subject_number_title[0],
                                                  subject_number_title[2], description))
                        i+=skipNextLine
                        break

        return course_list


# if __name__ == '__main__':
#     # http://www.concordia.ca/academics/undergraduate/calendar/current/courses-quick-links.html
#
#     CourseDataParser.extractCoursesFromFile("../CoursePagesHtml/AHSC.html",["AHSC"])



