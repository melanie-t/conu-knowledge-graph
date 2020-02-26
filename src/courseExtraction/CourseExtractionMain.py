from os import listdir, makedirs
from os.path import isfile, join, exists
import errno

from src.courseExtraction import CourseDataCollector
from src.courseExtraction.CourseDataParser import CourseDataParser


# Source: https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory/14364249#14364249
def make_sure_path_exists(path):
    try:
        makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
# End source

"""
This script extracts the courses contained in all the HTML pages saved in the folder 'CoursePagesHtml'.
"""
path_to_course_pages = 'CoursePagesHtml/'
make_sure_path_exists(path_to_course_pages)

acronyms_to_search = [
    ['AHSC'],['BIOL'],['CHEM'],
    ['CLAS','MARA','MCHI','GERM','ITAL','SPAN','LING','HEBR','MGRK','MIRI','MODL','MRUS'],
    ['COMS'],['SCPA'],['ECON'],
    ['EDUC','INST','LIBS','TESL','ESL','ADED'],
    ['ENGL'],['FRAA','FRAN','FLIT','FTRA'],
    ['FPST'],['GEOG','GEOL','URBS'],
    ['CATA','EXCI','KCEP'],['HIST','HISW'],
    ['INTE'],['SSDB','WSDB'],
    ['IRST'],['JOUR'],['LBCL'],
    ['LOYC'],['ACTU','MACF','MAST','MATH','STAT'],
    ['PHIL'],['PHYS'],['POLI'],['PSYC'],['RELI'],
    ['SCOL'],['SOCI','ANTH'],['THEO'],

    ['COMM'],['ACCO'],['ADMI'],['FINA'],
    ['IBUS'],['MANA'],['MARK'],
    ['BSTA','BTM','SCOM'],

    ['ENCS','ENGR','AERO','COEN','BCEE','BLDG','CIVI','ELEC','IADI','INDU','MECH'],
    ['COMP','SOEN'],

    ['ARTE'],['ARTH'],['FMST','FMAN','FMPR'],
    ['DANC'],['CATS','ATRP','DTHY','MTHY'],
    ['CART','DART'],['FFAR','FASS'],
    ['EAST','JAZZ','JHIS','JPER','MHIS','MPER','MUSI'],
    ['ARTX','ARTT','CERA','DRAW','FBRS','IMCA','PTNG','PHOT','PRIN','SCUL','VDEO'],
    ['ACTT','DFTT','PERC'],

    ['CWT'],

    ['UNSS']
]

path_to_courses = 'courses.txt'

if __name__ == '__main__':
    # Run CourseDataCollector
    CourseDataCollector.downloadAllHTML()

    files_from_dir = [f for f in listdir(path_to_course_pages) if isfile(join(path_to_course_pages, f))]

    file = open(path_to_courses, 'w', encoding="latin-1")

    for i in range(len(files_from_dir)):
        acronym_file = files_from_dir[i].split('.')[0]
        # find right acronym to search for based on name of file (if list of acronyms, match with first one)
        for j in range(len(acronyms_to_search)):
            if acronym_file == acronyms_to_search[j][0]:
                course_list = CourseDataParser.extractCoursesFromFile(path_to_course_pages+files_from_dir[i], acronyms_to_search[j])
                # write courses to file
                for k in range(len(course_list)):
                    file.write(str(course_list[k].subject)+' '+str(course_list[k].number)+' \"'+str(course_list[k].title)+'\" \"'+str(course_list[k].description)+'\"\n')
                    print(str(course_list[k].number)+' '+str(course_list[k].subject)+' '+str(course_list[k].title))
                print("Analysis of file "+files_from_dir[i]+" complete.")
                break

    file.close()