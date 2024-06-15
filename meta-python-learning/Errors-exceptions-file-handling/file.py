"""
Mode = 'r+ => Open for reading
Mode = 'w => Open for writing
open(file, a)  => Open for editing or appending data

close ()

with open('texting.txt', 'r') as file:
   .....


-------------- Binary format -----------

open(filename, rb)
open(filename, rb+)
open(filename, wb)
open(filename, ab)

"""


# file = open('test.txt', mode='r')
# data = file.readline()
# print(data)
#
# with open('test.txt', mode='r') as file:
#     data = file.readline()
#     print(data)
#
# #--------------- Creating files --------
# # To edit the file
# try:
#     with open('newfile.txt', 'w') as file:
#         file.writelines(["This is a new file created", "\nThis is another"])
# except FileNotFoundError as e:
#     print(e)
#
# # reading file---------------------
# with open('sample.txt', 'r') as file:
#     print(file.read())
#     print(file.read(40))
#
# # Readline method
# print(file.readline(10))
#
# #
# with open('testing.txt', 'r') as file:
#     lines = file.readline()
#     print(len(lines))
#     for line in lines:
#         print(line)
#

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    with open('newfile.txt', 'r') as file1:
        first_line = file1.readline(1)
        print(first_line)
