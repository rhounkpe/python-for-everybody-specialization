# Concatenating Lists Using +
"""
We can create a new list by addng two existing lists together
"""
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# Lists can be sliced using :
"""
Rememmber: Just like in strings, the second number is 'up to but not including'
"""
t = [9, 41, 12, 3, 74, 15]
t[1 : 3] # [41, 12]
t[: 4] # [9, 41, 12, 3]
t[3:] # [3, 74, 15]
t[:] # [9, 41, 12, 3, 74, 15]

# Building a list from scratch
"""
- We can create an empty list and then add element using the append method.
- The list stays in order and new elements are added at the end of the list.
"""
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff) # ['book', 99]
stuff.append('cookie')
print(stuff) # ['book', 99, 'cookie']

# Is something in a list?
"""
- Python provides two operators that let you check if an item is in a list
- These are logical operators that return True or False
- They do not modify the list
"""
some = [1, 9, 21, 10, 16]
9 in some # True
15 in some # False
20 not in some # True

# Lists are in Order
"""
- A list can hold many items and keeps those items in the order until we do something to change the order
- A list can be sorted (i.e., change its order)
- The sort method (unlike in strings) means 'sort yourself'
"""
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends) # ['Glenn', 'Joseph', 'Sally']
print(friends[1]) # Joseph

total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(input)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)


numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(input)
    numlist.append(value)

average = sum(numlist) / len(numlist)

print('Average:', average)