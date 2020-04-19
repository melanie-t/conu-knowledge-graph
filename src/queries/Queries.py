import os
import errno


def open_query_files(query_num):
    make_sure_path_exists("./output/")

    query_file_path = "./sparql_queries/" + f"{query_num}.txt"
    output_file_path = "./output/" + f"{query_num}_response.txt"

    query = open(query_file_path, "r")
    output = open(output_file_path, "w+")

    return query, output


def save_results(results, output_file):
    for row in results:
        result = ''
        for entry in row:
            result = result + str(entry) + ' '
        result = result + '\n'
        print(result)
        output_file.write(str(result))


# Source: https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory/14364249#14364249
# And https://github.com/melanie-t/COMP472_Project1_W20/blob/master/src/helper_functions.py
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
# End source
