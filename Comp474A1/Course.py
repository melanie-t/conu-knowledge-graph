import requests
import re
import string

class Course:
    def __init__(self, number, title, description):
        self.number = number
        self.title = title
        self.description = description

def return_first_match(text, regex):
    try:
        result = re.findall(regex, text)[0]
    except Exception as IndexError:
        result = ''
    return result


if __name__ == '__main__':
    r = requests.get("http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-70.html#compsci")
    source = r.text
    courseList = []
    result = re.findall(r"(<b>(.?)*[\s]*Prerequisite:(.?)*)", source)

    for (courseSource) in result:
        s = courseSource[0].encode("ascii", errors="ignore").decode()
        courseNum = return_first_match(s, r"<b>([a-zA-Z]+ [0-9]+)")
        courseTitle = return_first_match(s, r"[;|>]+[\s]*([a-zA-Z\s0-9\,]+)[\s]*[^<]*</i>")
        courseDesc = return_first_match(s, r"[\s]*(Prerequisite:[^<]+)[<br>|</p>]+")
        courseList.append(Course(courseNum, courseTitle, courseDesc))

    count = 1
    for obj in courseList:
        print("\n", count, ".1:", obj.number, "\n", count, ".2:", obj.title, "\n", count, ".3:", obj.description)
        count = count + 1
