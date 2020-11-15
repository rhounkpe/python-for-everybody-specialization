# Assignment 7.2 
"""
Write a program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form: X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines 
and compute the average of those values and produce an output as shown below. 
'Average spam confidence: 0.7507185185185187'
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
#
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
add_val = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    colpos = line.find(':')
    val = line[colpos + 1 : ]
    val = val.lstrip()
    val = float(val)
    add_val = add_val + val
    count = count + 1

print('Average spam confidence:', add_val / count)