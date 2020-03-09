import requests
import re

from src.courseExtraction.Course import Course

all_grad_urls = ["https://www.concordia.ca/academics/graduate/calendar/current/fasc/ahsc-dip.html#diploma-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/jour-visual-dip.html#vj-dip-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/ftra-ma.html#cours",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/ftra-dip.html#dip-cours",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/theo.html#courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/soci-ma.html#ma-sociology-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/socianth-ma.html#ma-social-cultural-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/reli-ma.html#MARelCourses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/poli-mpppa.html#mpppa-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/psyc-phd.html#courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/psyc-ma.html#courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/poli-phd.html#phd-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/phil.html#courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/coms-ma.html#courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/mast-phd.html#phd-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/mast-ma-msc.html#ma-msc-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/reli-judaic-ma.html#MAJudCourses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/jour-dip.html#vj-dip-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/adip-dip.html",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/chem-msc.html#courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/biol-phd.html#phd-msc-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/biol-msc.html#phd-msc-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/apli-ma.html",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/geog-phd.html#phdcourses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/geog-msc.html#msccourses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/geog-menv.html#courses-menv",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/geog-dip.html#dip-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/engl-phd.html#phd-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/engl-ma.html#courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/etec-ma.html",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/estu-ma.html#courses-ed-studies",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/educ-phd.html#PhDEd",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/econ-phd.html#courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/econ-ma.html#courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/scpa-ced.html#courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/coms-dip.html#elective-courses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/coms-phd.html#phdcourses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/chst-ma.html#MAChildCourses",
"https://www.concordia.ca/academics/graduate/calendar/current/fasc/chem-phd.html#courses",
"https://www.concordia.ca/academics/graduate/calendar/current/encs/engineering-courses.html",
"https://www.concordia.ca/academics/graduate/calendar/current/encs/computer-science-courses.html"]

file_names = 	['AHSC','JOUR','FTRA-MA','FTRA-CERT','THEO','SOCI','ANTH','RELI','POLI',
				'PSYC-PHD','PSYC-MA','POLI','PHIL','COMS','MAST-PHD','MAST-MA','RELI',
				'JOUR','ADIP','CHEM-MA','BIOL-PHD','BIOL-MSC','APLI','GEOG-PHD','GEOG-MSC',
				'GEOG-MENV','GEOG-MA','ENGL-PHD','ENGL-MA','ETEC','ESTU','EDUC','ECON-PHD',
				'ECON-MA','SCPA','COMS-MA','COMS-PHD','CHST','CHEM-PHD','ENGR','COMP']
path_to_course_pages = 'GraduateCoursePagesHtml/'
def return_first_match(text, regex):
    try:
        result = re.findall(regex, text)[0]
    except Exception as IndexError:
        result = ''
    return result
def file_get_contents(filename):
    with open(filename) as f:
        return f.read()
def downloadGradHTML():
    print('DOWNLOADING GRADUATE CLASSES')
    print('Same number of urls as file names? ', len(file_names) == len(all_grad_urls))

    for i in range(len(all_grad_urls)):
        response = requests.get(all_grad_urls[i])
        file = open('GraduateCoursePagesHtml/' + file_names[i] + '.html', 'w', encoding="latin-1")
        output = re.sub("&nbsp;", "", (response.text).encode("ascii", errors="ignore").decode())
        file.write(output)
        file.close()
def getUrlForCourseAcronym(courseAcronym):
    for i in range(len(file_names)):
        if file_names[i] == courseAcronym:
            return all_grad_urls[i]
    return ''

class GradCourseExtraction:
    @staticmethod
    def extractGradCourses():
        downloadGradHTML()
        courseList = []

        #for i in range(len(files_from_dir)):
        for i in range(len(file_names)):
            filePath = path_to_course_pages+file_names[i]+'.html'
            r = file_get_contents(filePath)
            source = re.sub("&nbsp;", "", r)
            result = re.findall(
                r"(<p><span class=\"large-text\"><b>[A-Z]+ [0-9]+ (.?)*[\s]*(<i>Prerequisite:(.?)*[\s]*)*(.?)*)",
                source)
            for (courseSource) in result:
                s = courseSource[0].encode("ascii", errors="ignore").decode()
                courseNum = return_first_match(s, r"<p><span class=\"large-text\"><b>([A-Za-z]+ [0-9]+)")  # 70
                number = return_first_match(s, r"[A-Za-z]+ ([0-9]+)")
                subject = return_first_match(s, r"([A-Za-z]+) [0-9]+")
                courseTitle = return_first_match(s, r"<p><span class=\"large-text\"><b>[A-Za-z]+ [0-9]+[\s]*([^<]*)")
                # courseDesc = return_first_match(s, r"<p><span class=\"large-text\"><b>[A-Z]+ [0-9]+ (.?)*[\s]*((.?)*)")[1]
                courseDesc = return_first_match(s,r"<p><span class=\"large-text\"><b>[A-Z]+ [0-9]+ (.?)*[\s]*((<i>Prerequisite:(.?)*[\s]*)*(.?)*)")[1]
                courseDesc2 = re.sub(r"<[^>]*>", "", courseDesc).replace('\n', ' ').replace('\r', '')
                courseList.append(Course(number, subject, courseTitle, courseDesc2))

        count = 1
        for obj in courseList:
            print("\n", count, ".1:", obj.number, "\n", count, ".2:", obj.subject, "\n", count, ".3:", obj.title, "\n",
                  count, ".4:", obj.description)
            count = count + 1
        print(len(courseList))

        return courseList