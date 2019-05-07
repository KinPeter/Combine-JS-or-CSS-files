"""
USAGE: 

1) First, in your main file, create a comment where you list all the relative pathes of the files you want to include in the bundle between "/*@include:" and "@end*/" tags, separated by commas, as in this example:
/*@include: ./modules/data.js, ./modules/lang.js, ./modules/page.js @end*/

2) Next, start the program with adding the full path to your main file as a "-f" or "--file" parameter, just as below: 
> python combine.py -f "C:\Projects\Work\Your_App\filename.js"

3) The program will create a new file with the name of "filename.bundle.js" in the same  directory where the main file is located.

Please note, unless you modify the code, in the new bundle file the included files will come first (in the order as you listed them in the comment), and the main file will be at the bottom.
"""

import re
import argparse

encoding = "utf-8"
comment_regex = re.compile("(?<=\/\*@include:)(.*)(?=@end\*\/)", re.MULTILINE)
new_file = ""

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="Full path to main JS file")
    options = parser.parse_args()
    return options

def get_list_of_add_files(text_to_parse):
    regex_result = re.findall(comment_regex, text_to_parse)
    list = regex_result[0].split(",")
    new_list = []
    for string in list :
        new_list.append( string.strip() )
    return new_list

def open_file(dir_path, filename):
    text = ""
    with open(dir_path + filename, "r", encoding=encoding) as file:
        for line in file:
            text += line
    return text

def parse_path(full_path):
    path = str(full_path).replace("\\", "/")
    list = path.split("/")
    filename = list.pop(-1)
    dirpath = ""
    for part in list:
        dirpath += part + "/"
    return [dirpath, filename]

def add_all_files(list):
    global dir_path
    global new_file
    for path in list:
        try: 
            content = open_file(dir_path, path)
        except FileNotFoundError:
            print("[-] Error: File flagged for inclusion not found.")
            print("[-] Please check the path of the files you want to include.")
            exit()
        new_file += "/*\n* included file: " + path + "\n*/\n\n"
        new_file += content + "\n\n\n"

def create_new_filename(filename):
    name, extension = filename.split(".")
    return name + ".bundle." + extension

def write_new_file(dir_path, new_filename, text):
    with open(dir_path + new_filename, "w", encoding=encoding) as file:
        file.write(text)



# get directory path and filename from the cmd argument
argument = get_arguments()
dir_path, filename = parse_path(argument.file)

# open the main file and save it in a variable
try:
    main_file = open_file(dir_path, filename)
except FileNotFoundError:
    print("[-] Error: File not found, please check the entered path.")
    exit()

# parse the main file and find the comment that contains the other filenames to be combined
try: 
    list = get_list_of_add_files(main_file)
except IndexError: 
    print("[-] Error: Couldn't read the list of files to include.")
    print("[-] Please check the comment syntax in your main file.")
    exit()

# add all files to the new_file string
add_all_files(list)

# add the main file to the end
new_file += "/*\n* MAIN file:\n*/\n\n"
new_file += main_file

# set output filename to name.bundle.ext
new_filename = create_new_filename(filename)

# create the output file:
write_new_file(dir_path, new_filename, new_file)

# and voila!
print("[+] Created new file: " + dir_path + new_filename)

