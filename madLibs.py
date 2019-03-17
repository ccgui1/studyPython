#!/usr/bin/env python3
import re
#read text
file = open('/root/studyPython/test.txt','r')
words = file.read()
file.close()
#find keywords
pattern = re.compile('ADJECTIVE|NOUN|VERB|ADVERB')
mo = pattern.findall(words)
print(mo)
#Replace each keyword in turn
for word in mo:
		repl = input(f'Enter a {word}:\n')
		regex = re.compile(word)
		words = regex.sub(repl,words,1)
print(words)
new_file = open('/root/studyPython/test2.txt','w')
new_file.write(words)
new_file.close()

