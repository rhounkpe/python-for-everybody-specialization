# Dictionaries
"""
- Lists index their entries based on the position in the list
- Dictionaries are like bags - no order
- SO we index the things we put in the dictionary with a 'lookup tag'
"""
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)

# When we see a new name
"""
When we encounter a new name, we need to add a new entry in the dictionary 
and if this is the second or later time we have seen the name,
we simly add one to the count in the dictionary under that name
"""
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)

# The get method for dictionaries
"""
The pattern of checking to see if a key is already in a dictionary and assuming a default value
if the key is not there is so common that there is a method called 'get()' that does this for us.

Default value if key does not exist (and no Traceback).
"""

"""
if n in names:
    x = counts[n]
else:
    x = 0

x = counts.get(name, 0)
"""

# Simplified counting with get()
"""
We can use get() and provide a default value of zero when the key is not yet in the dictionary - 
and then just add one.
"""

for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)