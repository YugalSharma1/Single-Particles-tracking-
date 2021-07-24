import os
import re

# a function to get a specific string with regEx from the files in all the directories in a given directory
def get_string_from_file(dir_path, regEx):
    dir_list = os.listdir(dir_path)
    print(dir_list)
    outfile = open('outfile2.csv', 'w')
    for file in dir_list:
        try:
            file_path = os.path.join(dir_path, file,'lagrangian','kinematicCloud','positions')
            _file = open(file_path, 'r')
            file_content = _file.read()
            #get the string
            string = re.findall(regEx, file_content)[0]
            string2 = string[1:-1]
            [x,y,z] = string2.split(' ')
            outfile.write(file + ',' + x + ',' + y + ',' + z + '\n')
            file.close()
        except:
            continue

# get the string from the file between ( )
get_string_from_file('./', '\(.*\)')
