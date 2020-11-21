name = input('Enter a file: ')

if len(name) < 1: name = "../material/mbox.txt"

try:
    data = open(name)
except:
    print('The file name ', name, ' does not exist!')
    quit()


dico = dict()
affiliation = dict()
 
addresses = []

for line in data:
    line = line.strip()

    if not line.startswith('From'): continue

    words = line.split()
    # print(words)
    for word in words:
   
        if '@' in word: 
            word = word.strip()
            worditems = word.split('@')
            name = worditems[0]
            instwithext = worditems[1]
            institems = instwithext.split('.') 
            inst = institems[0]
            
            if not name in affiliation:
                affiliation[name] = inst

            if not word in addresses:
                addresses.append(word)


        dico[word] = dico.get(word, 0) + 1

print(affiliation)
#print(addresses)
# print(dico.items())

bigcount = None
bigword = None

for k, v in dico.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v

print(bigword, bigcount)

