# Counting Pattern
"""
The general pattern to count the words in a line of text is to split
words in a line into words, then loop through the words and use 
a dictionary to track the count of each word independently.
"""
# Retrieving lists of keys and values
text = 'Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary - actually it goes through all of the keys in the dictionary and looks up the values.'
counts = dict()
print('Enter a line of text: ')


line = input('')

if len(line.rstrip()) == 0:
    line = text.rstrip()


words = line.split()
print('Words: ', words)

print('Counting...')

for word in words:
    counts[word] = counts.get(word, 0) + 1

print('Counts', counts)

# Definite Loops and Dictionaries
"""
Even though dictionaries are not stored in order, we can write a for loop
that goes through all the entries in a dictionary - 
actually it goes through all of the keys in the dictionary and looks up the values
"""

new_counts = { 'chuck': 1, 'fred': 42, 'jan': 100 }
for key in new_counts:
    print(key, new_counts[key])


# Retrieving lists of keys and values
"""
You can get a list of keys, values, or items (both) from a dictionary.
"""
jjj = { 'chuck': 1, 'fred': 42, 'jan': 100 }
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())


# Two Iteration variables
"""
- We loop through the key-value pairs in a dictionary using *two* iteration variables.
- Each iteration, the first variable is the key and the second variable is the corresponding value for the key.
"""

for k, v in jjj.items():
    print(k, v)