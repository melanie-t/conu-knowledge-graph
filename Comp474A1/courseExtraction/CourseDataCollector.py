import requests

"""
This script gets all the HTML files from the Internet for us to get the content that will eventually allow us to extract
the courses on the web pages.

FROM http://www.concordia.ca/academics/undergraduate/calendar/current/courses-quick-links.html :

FACULTY OF ARTS AND SCIENCE:
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-010.html#courses AHSC
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-030.html#courses BIOL
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-050.html#courses CHEM
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-060.html CLAS,MARA,MCHI,GERM,ITAL,SPAN,LING,HEBR,MGRK,MIRI,MODL,MRUS
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-070.html#courses COMS
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-540.html#scpa-courses SCPA
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-080.html#courses ECON
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-090.html EDUC,INST,LIBS,TESL,ESL,ADED
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-100.html#courses ENGL
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-110.html FRAA,FRAN,FLIT,FTRA
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-540.html#fpst-courses FPST
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-130.html GEOG,GEOL,URBS
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-120.html CATA,EXCI,KCEP
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-160.html#courses HIST,HISW
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-170.html#courses INTE
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-560.html SSDB,WSDB
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-530.html#courses IRST
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-180.html#courses JOUR
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-520.html#courses LBCL
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-525.html#courses LOYC
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-200.html ACTU,MACF,MAST,MATH,STAT
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-220.html#courses PHIL
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-230.html#courses PHYS
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-240.html#courses POLI
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-250.html#courses PSYC
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-270.html#courses RELI
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-550.html#scol-courses SCOL
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-310.html#soci-courses SOCI,ANTH
http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-330.html#courses THEO

JOHN MOLSON SCHOOL OF BUSINESS:
http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-10.html#b61.35 COMM
http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-40.html#courses ACCO
http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-120.html#courses ADMI
http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-70.html#courses FINA
http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-80.html#courses IBUS
http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-90.html#courses MANA
http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-100.html#courses MARK
http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-50.html BSTA,BTM,SCOM

GINA CODY SCHOOL OF ENGINEERING AND COMPUTER SCIENCE (ALL IN ONE PAGE, EXCEPT COMP AND SOEN):
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html#encs ENCS
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html#engr ENGR
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html#aero AERO
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html#bcee BCEE
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html#bldg BLDG
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html#civi CIVI
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html#coen COEN
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-70.html#compsci COMP
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html#elec ELEC
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html#iadi IADI
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html#indu INDU
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html#mech MECH
http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-70.html#softeng SOEN

FACULTY OF FINE ARTS:
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-40.html#courses ARTE
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-50.html#courses ARTH
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-60.html#filmstud FMST
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-60.html#filmanim FMAN
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-60.html#filmprod FMPR
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-70.html#courses DANC
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-80.html CATS,ATRP,DTHY,MTHY
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-90.html#comparts CART
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-90.html#designart DART
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-10.html#b81.30 FFAR
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-10.html#fass FASS
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-100.html EAST,JAZZ,JHIS,JPER,MHIS,MPER,MUSI
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-110.html ARTX,ARTT,CERA,DRAW,FBRS,IMCA,PTNG,PHOT,PRIN,SCUL,VDEO
http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-120.html ACTT,DFTT,PERC

INSTITUTE FOR CO-OPERATIVE EDUCATION:
http://www.concordia.ca/academics/undergraduate/calendar/current/sec24.html#cwt-courses CWT

UNIVERSITY SKILLS:
http://www.concordia.ca/academics/undergraduate/calendar/current/sec26.html#unss-courses UNSS
"""

all_urls = [
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-010.html", #AHSC
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-030.html", #BIOL
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-050.html", #CHEM
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-060.html", #CLAS,MARA,MCHI,GERM,ITAL,SPAN,LING,HEBR,MGRK,MIRI,MODL,MRUS
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-070.html#courses", #COMS
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-540.html#scpa-courses", #SCPA
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-080.html#courses", #ECON
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-090.html", #EDUC,INST,LIBS,TESL,ESL,ADED
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-100.html#courses", #ENGL
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-110.html", #FRAA,FRAN,FLIT,FTRA
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-540.html#fpst-courses", #FPST
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-130.html", #GEOG,GEOL,URBS
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-120.html", #CATA,EXCI,KCEP
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-160.html#courses", #HIST,HISW
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-170.html#courses", #INTE
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-560.html", #SSDB,WSDB
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-530.html#courses", #IRST
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-180.html#courses", #JOUR
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-520.html#courses", #LBCL
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-525.html#courses", #LOYC
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-200.html", #ACTU,MACF,MAST,MATH,STAT
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-220.html#courses", #PHIL
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-230.html#courses", #PHYS
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-240.html#courses", #POLI
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-250.html#courses", #PSYC
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-270.html#courses", #RELI
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-550.html#scol-courses", #SCOL
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-310.html#soci-courses", #SOCI,ANTH
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec31/31-330.html#courses", #THEO

    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-10.html#b61.35",  #COMM
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-40.html#courses", #ACCO
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-120.html#courses", #ADMI
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-70.html#courses", #FINA
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-80.html#courses", #IBUS
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-90.html#courses", #MANA
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-100.html#courses", #MARK
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec61/61-50.html", #BSTA,BTM,SCOM

    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-60.html", #ENCS,ENGR,AERO,COEN,BCEE,BLDG,CIVI,ELEC,IADI,INDU,MECH
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-70.html", #COMP,SOEN

    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-40.html#courses", #ARTE
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-50.html#courses", #ARTH
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-60.html", #FMST,FMAN,FMPR
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-70.html#courses", #DANC
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-80.html", #CATS,ATRP,DTHY,MTHY
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-90.html#comparts", #CART,DART
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-10.html", #FFAR,FASS
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-100.html", #EAST,JAZZ,JHIS,JPER,MHIS,MPER,MUSI
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-110.html", #ARTX,ARTT,CERA,DRAW,FBRS,IMCA,PTNG,PHOT,PRIN,SCUL,VDEO
    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec81/81-120.html", #ACTT,DFTT,PERC

    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec24.html#cwt-courses", #CWT

    "http://www.concordia.ca/academics/undergraduate/calendar/current/sec26.html#unss-courses" #UNSS
]

file_names = [
    'AHSC', 'BIOL', 'CHEM', 'CLAS', 'COMS', 'SCPA', 'ECON', 'EDUC', 'ENGL', 'FRAA', 'FPST', 'GEOG', 'CATA', 'HIST',
    'INTE', 'SSDB', 'IRST', 'JOUR', 'LBCL', 'LOYC', 'ACTU', 'PHIL', 'PHYS', 'POLI', 'PSYC', 'RELI', 'SCOL', 'SOCI',
    'THEO',

    'COMM', 'ACCO', 'ADMI', 'FINA', 'IBUS', 'MANA', 'MARK', 'BSTA',

    'ENCS', 'COMP',

    'ARTE', 'ARTH', 'FMST', 'DANC', 'CATS', 'CART', 'FFAR', 'EAST', 'ARTX', 'ACTT',

    'CWT',

    'UNSS'
]

print('Same number of urls as file names? ',len(file_names) == len(all_urls))

for i in range(len(all_urls)):
    response = requests.get(all_urls[i])
    file = open('../CoursePagesHtml/'+file_names[i]+'.html','w')
    file.write(response.text)
    file.close()