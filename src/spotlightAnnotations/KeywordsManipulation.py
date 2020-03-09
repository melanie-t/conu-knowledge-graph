
class KeywordsManipulation:
    input_file_URI = '../spotlight-keywords.txt'
    output_file_URI = '../spotlight-set.txt'

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
        output_file = open(KeywordsManipulation.output_file_URI, 'w')
        for i in range(len(keywords_uris)):
            output_file.write(keywords_uris[i][KEYWORD_INDEX]+" "+keywords_uris[i][URI_INDEX]) # \n already included with URI
        output_file.close()

    @staticmethod
    def getSetOfKeywords(): # assumes set of keywords already exists
        KEYWORD_INDEX = 0
        KEYWORD_INDEX_FILE = 0
        URI_INDEX = 1
        URI_INDEX_FILE = 1

        keywords_uris = []
        input_file = open(KeywordsManipulation.output_file_URI, 'r')
        for line in input_file:
            keyword_uri_literals = line.split("\" ")
            keyword_uri = [0 for i in range(2)]
            keyword_uri[KEYWORD_INDEX] = keyword_uri_literals[KEYWORD_INDEX_FILE] + "\""  # removes it in split
            keyword_uri[URI_INDEX] = keyword_uri_literals[URI_INDEX_FILE]
            keywords_uris.append(keyword_uri)

        return keywords_uris


if __name__ == '__main__':
    #KeywordsManipulation.generateSetOfKeywords()
    setK = KeywordsManipulation.getSetOfKeywords()
    print(len(setK))