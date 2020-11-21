# Assignment 9.4
"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = input("Enter file:")
# Read through the mbox-short.txt
# if len(name) < 1 : name = "mbox-short.txt"
if len(name) < 1: name = "../material/mbox-short.txt"
handle = open(name)

# Creates a Python dictionary
dico = dict()

for line in handle:
    line = line.strip()
    # Looks for 'From ' lines
    if not line.startswith( 'From '): continue
    # print(line)
    words = line.split()
    # Takes the second word of those lines as the person who sent the mail.
    person = words[1]
    # print(person)

    # Maps the sender's mail address to a count of the number of times they appear in the file
    dico[person] = dico.get(person, 0) + 1

print(dico.items())
"""
After the dictionary is produced, the program reads through 
the dictionary using a maximum loop to find the most prolific committer.
"""
# Figure out who has sent the greatest number of mail messages.
most_prolific_committer = None # cwen@iupui.edu
frequency = None # 10

for k, v in dico.items():
    if frequency is None or frequency < v:
        most_prolific_committer = k
        frequency = v

print(most_prolific_committer, frequency)