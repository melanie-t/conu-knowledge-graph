from courseExtraction.CourseExtractorFromTxt import CourseExtractorFromTxt

class KeywordsManipulation:
    input_file_URI = '../spotlight-keywords.txt'
    set_file_URI = '../spotlight-set.txt'
    relationToCourse_file_URI = '../spotlight-linkCourse.txt'

    @staticmethod
    def generateSetOfKeywords():
        KEYWORD_INDEX = 0
        KEYWORD_INDEX_FILE = 0
        URI_INDEX = 1
        URI_INDEX_FILE = 1
        HASH_INDEX = 2
        input_file = open(KeywordsManipulation.input_file_URI, 'r')
        keywords_uris = []
        i=0 # index
        for line in input_file:
            keyword_uri_literals = line.split("\" ")
            keyword_uri = [0 for i in range(3)]
            keyword_uri[KEYWORD_INDEX] = keyword_uri_literals[KEYWORD_INDEX_FILE]+"\"" # removes it in split
            keyword_uri[URI_INDEX] = keyword_uri_literals[URI_INDEX_FILE]
            keyword_uri[HASH_INDEX] = hash(keyword_uri[KEYWORD_INDEX])

            is_in_list = False
            for j in range(len(keywords_uris)):
                if keywords_uris[j][HASH_INDEX] == keyword_uri[HASH_INDEX]:
                    if keywords_uris[j][KEYWORD_INDEX] == keyword_uri[KEYWORD_INDEX]:
                        is_in_list = True
                        break

            if not is_in_list:
                keywords_uris.append(keyword_uri)

            print(i)
            i+=1
        input_file.close()
        # output
        output_file = open(KeywordsManipulation.set_file_URI, 'w')
        for i in range(len(keywords_uris)):
            output_file.write(keywords_uris[i][KEYWORD_INDEX]+" "+keywords_uris[i][URI_INDEX]) # \n already included with URI
        output_file.close()

    @staticmethod
    def generateHash(string_keyword):
        words_in_keyword = string_keyword.split(" ")
        #takes only first word into consideration
        hash_val = hash(words_in_keyword[0])
        return hash_val, len(words_in_keyword)

    @staticmethod
    def __build_keyword(nb_words, starting_index, words_list):
        if nb_words > 1:  # build string
            keyword = ""
            for l in range(nb_words):
                if len(words_list) == starting_index + l: # out of bounds
                    return ""
                keyword += words_list[starting_index + l]
                if l != nb_words - 1:
                    keyword += " "
            return keyword
        else:
            return words_list[starting_index]

    @staticmethod
    def __analyze_string_for_keyword(string_analyzed, set_keywords, hashes_N_count):
        KEYWORD_INDEX = 0
        HASH_INDEX = 0
        NB_WORDS_IN_KEYWORD_INDEX = 1
        # entry in result_list
        index_keywords = []
        # title inspection
        words = string_analyzed.split(" ")
        for j in range(len(words)):
            hash_word = hash(words[j])
            for k in range(len(set_keywords)):
                if hash_word == hashes_N_count[k][HASH_INDEX]:  # if first word is same
                    keyword = KeywordsManipulation.__build_keyword(
                        hashes_N_count[k][NB_WORDS_IN_KEYWORD_INDEX], j, words)
                    if keyword != "" and keyword == set_keywords[k][KEYWORD_INDEX]:
                        index_keywords.append(k)
        return index_keywords

    @staticmethod
    def generateLinksToCourseDescriptionAndTitle(): # generates a file
        KEYWORD_INDEX = 0
        URI_INDEX = 1
        set_keywords = KeywordsManipulation.getSetOfKeywords()
        courses_list = CourseExtractorFromTxt.get_course_list()

        # based on index of set_keywords. Each index can have multiple entries, depending on how many course description
        # or title contain a certain keyword
        result_list = [set() for i in range(len(set_keywords))]

        # generate hash for each keyword
        hashes_and_count_keyword = []
        for i in range(len(set_keywords)):
            hash, count_words = KeywordsManipulation.generateHash(set_keywords[i][KEYWORD_INDEX])
            hashes_and_count_keyword.append([hash, count_words])

        # compare keywords to text
        for i in range(len(courses_list)):
            index_keywords = KeywordsManipulation.__analyze_string_for_keyword(courses_list[i].title, set_keywords,
                                                              hashes_and_count_keyword)
            index_keywords_description = KeywordsManipulation.__analyze_string_for_keyword(courses_list[i].description,
                                                                set_keywords, hashes_and_count_keyword)
            for j in range(len(index_keywords)):
                result_list[index_keywords[j]].add(courses_list[i].subject+"/"+courses_list[i].number)
            for j in range(len(index_keywords_description)):
                result_list[index_keywords_description[j]].add(courses_list[i].subject+"/"+courses_list[i].number)

            print(i) # debug purposes

        # put content to file
        output_file = open(KeywordsManipulation.relationToCourse_file_URI, 'w')
        for i in range(len(result_list)):
            list_URI_paths = ""
            for j in result_list[i]:
                list_URI_paths+=j+","
            output_file.write("\""+set_keywords[i][KEYWORD_INDEX]+"\" "+set_keywords[i][URI_INDEX].rstrip()+" ["+
                              list_URI_paths[:-1]+"]\n")

        output_file.close()

    @staticmethod
    def getSetOfKeywords(): # assumes set of keywords already exists
        KEYWORD_INDEX = 0
        KEYWORD_INDEX_FILE = 0
        URI_INDEX = 1
        URI_INDEX_FILE = 1

        keywords_uris = []
        input_file = open(KeywordsManipulation.set_file_URI, 'r')
        for line in input_file:
            keyword_uri_literals = line.split("\" ")
            keyword_uri = [0 for i in range(2)]
            keyword_uri[KEYWORD_INDEX] = keyword_uri_literals[KEYWORD_INDEX_FILE][1:] # remove second double quote in split
            keyword_uri[URI_INDEX] = keyword_uri_literals[URI_INDEX_FILE]
            keywords_uris.append(keyword_uri)

        return keywords_uris


if __name__ == '__main__':
    #KeywordsManipulation.generateSetOfKeywords()
    #setK = KeywordsManipulation.getSetOfKeywords()
    #print(len(setK))
    KeywordsManipulation.generateLinksToCourseDescriptionAndTitle()