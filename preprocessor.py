import os
import sys


# source folder
source = './tensorflow/'
# destination file
destination = './tensorflow.txt'

def copy_files_to_single_file(source, destination):
    with open(destination, 'w') as outfile:
        for root, dirs, files in os.walk(source):
            for file in files:
                file_path = os.path.join(root, file)
                file_name = file

                if file_name.endswith('.py'):
                    with open(file_path, 'r') as infile:
                        outfile.write(infile.read())

if __name__ == '__main__':
    copy_files_to_single_file(source, destination)