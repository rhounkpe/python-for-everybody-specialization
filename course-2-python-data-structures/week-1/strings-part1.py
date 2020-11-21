# Looking inside Strings
#
fruit = 'banana'
letter = fruit[1]
print(letter) # a

x = 3
w = fruit[x - 1]
print(w) # n

print(len(fruit))


# Looping through Strings
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# For in loop
for letter in fruit:
    print(letter)


# Looping and counting
word = 'banana'
count = 0

for letter in word:
    if letter == 'a':
        count = count + 1

print(count)


count_b = 0
while count_b < len(word):
    letter = word[count]
    if(letter == 'a'):
        count_b = count_b + 1
    

s = 'Monty Python'
print(s[0:4]) # Mont
print(s[6:7]) # P
print(s[6:20]) # Python
print(s[:2]) # Mo
print(s[8:]) # thon
print(s[:]) # Monty Python