from pprint import pprint
import os

path = '.'

def create_combined_file(file_directory="."):
    if file_directory == "." or file_directory[-1] == '\\':
        file_list = os.listdir(file_directory)
        file_dict = {}
        # print(file_list)
        for file in file_list:
            if file.endswith('.txt'):
                # print(file)
                with open(file_directory + '/' + file, encoding='utf-8') as f:
                    # print(f.readlines())
                    counter = 0
                    data = f.readlines()
                    for line in data:
                        counter +=1
                        file_dict[file] = (counter, data)

                    with open('Final file.txt', 'w', encoding='utf-8') as f:
                        f.write(f'{file_dict}')


        pprint(file_dict)
    else:
        print('Такой папки нет')


create_combined_file(path)

