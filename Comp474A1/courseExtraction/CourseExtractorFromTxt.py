"""
This script will read the courses.txt file to be able to return the list of courses in the
form of Course objects
"""
from venv.courseExtraction.Course import Course

class CourseExtractorFromTxt:
    path_to_courses = 'courses.txt'

    @staticmethod
    def __create_course_from_data(line):
        first_instance_doublequote = line.find('\"') # before that it is course subject and number
        subject_number = line[0:first_instance_doublequote].split(" ")
        title_description = line[first_instance_doublequote:].split("\"")
        course = Course(subject_number[1], subject_number[0], title_description[1], title_description[3])
        return course

    @staticmethod
    def get_course_list():
        courses_file = open(CourseExtractorFromTxt.path_to_courses, 'r')
        courses_list = []
        for line in courses_file:
            courses_list.append(CourseExtractorFromTxt.__create_course_from_data(line))
        return courses_list

"""
if __name__ == '__main__':
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    CourseExtractorFromTxt.get_course_list()
"""