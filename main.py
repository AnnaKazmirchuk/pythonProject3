from pprint import pprint
import os


path = '.'

def writing_file(file_directory = "."):
    if file_directory == "." or file_directory[-1] == '\\':
        file_list = os.listdir(file_directory)
        # print(file_list)
        data = {}
        for files in file_list:
            if files.endswith('.txt'):
                with open(files, encoding='utf-8') as file:
                    line = file.read().split('\n')
                    # print(line)
                    data[files] = (len(line), line)
        for number, lines in sorted(data.values()):
            with open('result.txt', 'a', encoding='utf-8') as file:
                file.writelines("%s\n" % line for line in lines)
        return file
    else:
        print('Такой папки нет')

writing_file(path)