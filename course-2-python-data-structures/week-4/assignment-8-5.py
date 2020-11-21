# Assignment 8.5
"""
Open the file mbox-short.txt and read it line by line. 
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() 
and print out the second word in the line (i.e. the entire address of the person who sent the message). 
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
# fname = '../material/mbox-short.txt'

# Open the file mbox-short.txt and read it line by line.
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "../material/mbox-short.txt"

try:
    fh = open(fname)
except:
    print('The file ', fname, ' does not exists!')

count = 0

for line in fh:
    # When you find a line that starts with 'From ',
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    # You will parse the From line using split()
    words = line.split()
    # print out the second word in the line
    print(words[1])
    count = count + 1

#Print out a count at the end.
print("There were", count, "lines in the file with From as the first word")
