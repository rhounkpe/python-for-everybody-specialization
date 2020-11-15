# Best friends: strings and lists
abc = 'With three words'
stuff = abc.split()
print(stuff) #  ['With', 'three', 'words']
print(len(stuff)) # 3
print(stuff[0]) # With

"""
Split breaks a string into parts and produces a list of strings.
We think of these as words. We can access a particular word or loop through all words.

- When you do not specify a delimiter, multiple spaces are treated like one delimiter
- You can specify what delimiter character to use in the splitting.
"""
line = 'A lot      of    spaces'
etc = line.split() # ['A', 'lot', 'of', 'spaces']
line = 'first;second;third'
thing = line.split()
print(thing) # ['first;second;third']
print(len(thing)) # 1
#
thing = line.split(';')
print(thing) # ['first', 'second', 'third']
print(len(thing))

# Open file
mbox_short = open('../material/mbox-short.txt')
# Read fileLists and strings
git push

mbox = open('../material/mbox.txt')

for line in mbox_short:
    line = line.rstrip()
    if not line.startswith('From '): 
        continue
    words = line.split()
    print(words[2])

# The double split pattern
"""
Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again.
"""
# words = line.split()
# email = words[1]
# pieces = email.split('@')