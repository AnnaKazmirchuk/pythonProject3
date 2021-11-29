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
        # pprint(data)
        for numbers, lines in sorted(data.items(), key = lambda x:x[1][0]):
            print(numbers, lines)
            with open('result.txt', 'a', encoding='utf-8') as file:
                file.write(f'{numbers}\n')
                file.write(f"{lines[0]}\n")
                for string in lines[1]:
                    file.write(f'{string}\n')


        return file
    else:
        print('Такой папки нет')

writing_file(path)