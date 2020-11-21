"""
- A collection allows us to put many values in a single 'variable.
- A collection is nice beacause we can carry many values
  around in one convenient package.
"""

friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['soks', 'shirt', 'perfume']

# List Constants
"""
- List constants are surrounded by square brackets and the elements
  in the list are separated by commas

- A list element can be any Python object - even another list

- A list can be empty
"""
# print([1,24, 76])
# print(['red', 'yellow', 'blue'])
# print([1, [5, 6], 7])
# print([])

# Lists and definite Loops - Best Pals

for friend in friends:
    print('Happy new year:', friend)

print('Done!')

# Looking inside lists
"""
Just like strings, we can get at any single element in a list using an index
specified in square brackets
"""
print(friends[1]) # Glenn

#
# Lists are mutable
"""
- Strings are 'immutable' - we cannot change the contents of a string - 
  we must make a new string to make any change.

- Lists are 'mutable' - we can change an element of a list using the index operator.
"""

# A Tale of two Loops...
for friend in friends:
    print(friends)

# Counted loop
for i in range(len(friends)):
    friend = friends[i]
    print(i, friend)