
'''
This script scans all files within a directory and its sub-directories,
looking for a pattern within filesand prints out the matched string and its path location.
re and os modules are needed for this script.
Two global variables to define: Pattern and Path.
The first uses the function re.compile that returns a
pattern object that can be stored into a variable.
The latter is the path of the main directory you want the scanto start.
Note the path will have different format depending on which operative system you are using.
Use os.cwd() to check your current working directory and format.
'''

import os
import re

PATTERN = re.compile(r'---some--pattern---')
PATH = '/Users/some_name/....'

def scan_for_pattern(pattern, path):

    '''
    Function that takes 2 arguments: path of your target directory
    and regular expression pattern you need to look for.
    Will then start a nested for loops using directory tree generator function,
    os.walk() and for each file within the directory and its subdirectories
    will try to read their content and will compare it with the pattern you are looking
    for through the re.search() function. It will then try to generate the matched string,
    and if there are no matched, it will just be a Nonetype,
    else will print out the path and your matched string!
    '''

    for dir_path, dir_names, file_names in os.walk(path):

        for sub_folder in dir_names:
            pass

        for file in file_names:

            with open(os.path.join(dir_path, file), 'r') as file_screened:
                content = file_screened.read()
                match = re.search(pattern, content)

                try:
                    match.group()
                except AttributeError:
                    pass
                else:
                    matched = match.group()
                    print(f'Your match is in {dir_path}/{file} and it is: \t {matched}')
                


