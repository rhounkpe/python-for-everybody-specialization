# Assignment 8.4
"""
Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""
# fname = '../material/romeo.txt'
fname = input("Enter file name: ")

# Open the file romeo.txt
try:
    fh = open(fname)
except:
    print('The filename', fname, ' does not exist!')
    quit()
    
lst = list()
# read it line by line
for line in fh:
    # For each line, split the line into a list of words using the split() method.
    wordslist = line.split()
    # For each word on each line check to see if the word is already in the list and if not append it to the list.
    for word in wordslist:
        if word not in lst:
            lst.append(word)

# When the program completes, sort and print the resulting words in alphabetical order.
lst.sort()
print(lst)
