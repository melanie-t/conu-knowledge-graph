from src.studentCreation.StudentCourseEntry import StudentCourseEntry
from src.studentCreation.Term import Term

class Student:
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email
        self.curriculum = []

    def addCourseToCurriculum(self, subject, number, term_season, year, grade):
        term = Term(term_season, year)
        student_course_entry = StudentCourseEntry(subject, number, term, grade)
        self.curriculum.append(student_course_entry)