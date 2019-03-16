#!/usr/bin/env python3
import shelve,pprint,myCats

helloFile = open('/root/hello.txt')
helloContent = helloFile.read()
print(helloContent)

sonnetFile = open('/root/sonnet29.txt')
print(sonnetFile.readlines())


baconFile = open('/root/bacon.txt','w')
baconFile.write('Hello world!\n')
baconFile.close()
baconFile = open('/root/bacon.txt','a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('/root/bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

shelfFile = shelve.open('/root/mydata')
cats = ['Zophie','Pooka','Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('/root/mydata')
type(shelfFile)
print(shelfFile['cats'])
shelfFile.close()

cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
print(pprint.pformat(cats))
fileObj = open('/root/myCats.py','w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
fileObj = open('/root/myCats.py')
context = fileObj.read()
fileObj.close()
print(context)

print(myCats.cats)
print(myCats.cats[0]['name'])
