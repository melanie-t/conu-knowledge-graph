from venv.studentCreation.Student import Student
from venv.studentCreation.Term import TermSeasons


class StudentGenerator:
    student_list = []

    @staticmethod
    def __generate_students():
        student1 = Student('Roger Moores', '100000', 'roger@moores.ca')
        student2 = Student('Bianca Patry', '211111', 'bianca@concordia.ca')
        student3 = Student('Bob Sophomore', '333333', 'bob123@gmail.com')
        student4 = Student('Frank Gye', '422222', 'frank@outlook.com')
        student5 = Student('Julie Snyder', '999999', 'julie@snyder.com')
        student6 = Student('Florence Spiri', '666666', 'spiri101@gmail.com')
        student7 = Student('George Soros', '548888', 'spirit0fwind@outlook.com')
        student8 = Student('Alejandro Rojas', '674444', 'gonebytheminute@rojas.com')
        student9 = Student('Jordan Sala', '143333', 'jordan@sala.ca')
        student10 = Student('Giovanni Price', '926211', 'giovanni@concordia.ca')
        return [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]

    @staticmethod
    def generate_students_classes():
        student_list = StudentGenerator.__generate_students()
        student_list[1].addCourseToCurriculum('COMP',108, TermSeasons.FALL, '2019',85)
        student_list[1].addCourseToCurriculum('ADED',202,TermSeasons.SUMMER, '2016', 70)
        student_list[1].addCourseToCurriculum('TESL',491,TermSeasons.SUMMER,'2015',72)
        student_list[2].addCourseToCurriculum('AHSC',400,TermSeasons.WINTER,'2018',90)
        student_list[2].addCourseToCurriculum('ADED',202,TermSeasons.SUMMER,'2015',75)
        student_list[2].addCourseToCurriculum('UNSS',200,TermSeasons.FALL,'2012',88)
        student_list[3].addCourseToCurriculum('ADED',202,TermSeasons.FALL,'2014',55)
        student_list[3].addCourseToCurriculum('COMP',326,TermSeasons.FALL, '2010',32)
        student_list[3].addCourseToCurriculum('SSDB',428,TermSeasons.WINTER,'2008',43)
        student_list[4].addCourseToCurriculum('TESL',491,TermSeasons.SUMMER,'2001',95)
        student_list[4].addCourseToCurriculum('WSDB',298,TermSeasons.SUMMER,'2007',99)
        student_list[4].addCourseToCurriculum('COMP',108,TermSeasons.WINTER,'2005',89)
        student_list[5].addCourseToCurriculum('ARTH',263,TermSeasons.FALL,'2010',78)
        student_list[5].addCourseToCurriculum('EXCI',453,TermSeasons.WINTER,'2015',87)
        student_list[5].addCourseToCurriculum('EXCI',455,TermSeasons.WINTER,'2007',67)
        student_list[6].addCourseToCurriculum('EXCI',204,TermSeasons.FALL,'2011',83)
        student_list[6].addCourseToCurriculum('EXCI',218,TermSeasons.SUMMER,'2012',81)
        student_list[6].addCourseToCurriculum('CATA',365,TermSeasons.FALL,'2008',84)
        student_list[7].addCourseToCurriculum('THEO',201,TermSeasons.SUMMER,'2001',85)
        student_list[7].addCourseToCurriculum('THEO',212,TermSeasons.FALL,'2009',87)
        student_list[7].addCourseToCurriculum('THEO',298,TermSeasons.WINTER,'2011',100)
        student_list[8].addCourseToCurriculum('POLI',353,TermSeasons.WINTER,'2011',65)
        student_list[8].addCourseToCurriculum('THEO',298,TermSeasons.WINTER,'2011',78)
        student_list[8].addCourseToCurriculum('CHEM',203,TermSeasons.SUMMER,'2011',79)
        student_list[9].addCourseToCurriculum('CHEM',217,TermSeasons.SUMMER,'2019',45)
        student_list[9].addCourseToCurriculum('CHEM',217,TermSeasons.FALL,'2019',70)
        student_list[9].addCourseToCurriculum('FPST',415,TermSeasons.FALL,'2019',65)