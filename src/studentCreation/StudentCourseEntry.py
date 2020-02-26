class StudentCourseEntry:
    def __init__(self, subject, number, term, grade):
        self.subject = subject
        self.number = number
        self.term = term
        self.grade = grade

    def getTermSemester(self):
        return {
            0: 'FALL',
            1: 'WINTER',
            2: 'SUMMER'
        }[self.term.term_season]