# 7.1 Write a program that prompts for a file name, 
# then opens that file and reads through the file, 
# and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt
#
# Get the file name
filename = input('Enter file name: ')

# Try to open file. If filename does not exist, quit
try:
    fhand = open(filename)
except:
    print('File ', filename, ' do not exist...')
    quit()

# Filename exists. So read it.
for line in fhand:
    line = line.strip()
    line = line.upper()
    print(line)