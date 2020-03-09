from spotlight.SpotlightAssociations import SpotlightAssociations
from spotlight.QueryServer import QueryServer

if __name__ == '__main__':
    SpotlightAssociations.write_all_keywords_to_file_("../spotlight-keywords.txt",
                                                     "courses.txt",
                                                     "http://localhost:8080/rest/annotate",
                                                     0.35,
                                                      0)
