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
