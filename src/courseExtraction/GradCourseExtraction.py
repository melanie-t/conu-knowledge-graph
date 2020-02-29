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

def return_first_match(text, regex):
    try:
        result = re.findall(regex, text)[0]
    except Exception as IndexError:
        result = ''
    return result

class GradCourseExtraction:
    @staticmethod
    def extractGradCourses():
        courseList = []
        for i in range(len(all_grad_urls)):
            p = all_grad_urls[i]
            print(p)
            r = requests.get(p)
            source = re.sub("&nbsp;", "", r.text)
            # result = re.findall(r"(<p><span class=\"large-text\"><b>[A-Z]+ [0-9]+ (.?)*[\s]*(.?)*)", source)
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
                courseDesc2 = re.sub(r"<[^>]*>", "", courseDesc)
                courseList.append(Course(number, subject, courseTitle, courseDesc2))

        count = 1
        for obj in courseList:
            print("\n", count, ".1:", obj.number, "\n", count, ".2:", obj.subject, "\n", count, ".3:", obj.title, "\n",
                  count, ".4:", obj.description)
            count = count + 1
        print(len(courseList))

        return courseList