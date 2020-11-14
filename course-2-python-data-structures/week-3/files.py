# Open file
mbox_short = open('../material/mbox-short.txt')
inp = mbox_short.read()
#
# Read file
mbox = open('../material/mbox.txt') # 132045 lines

count = 0

for line in mbox:
    count = count + 1

print('Line count: ', count)

# Searching through a file
for line in mbox_short:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# Skipping with Continue
for line in mbox_short:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# Using in to Select lines
for line in mbox_short:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

# Prompt for file name and handle bad file names

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'Subject lines in', fname)