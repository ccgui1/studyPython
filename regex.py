#!/usr/bin/env python3
import re
nameRegex = re.compile(r'FirstName: (.*) Last Name: (.*)')
mo = nameRegex.search('FirstName: A1 Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man>for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man>for dinner.>')
print(mo.group())

noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newlineRegex = re.compile('.*',re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

robocop = re.compile(r'robocop',re.I)
print(robocop.search('RoboCop is part man,part machine,all cop.').group())

print(robocop.search('ROBOCOP protects the innocent.').group())

print(robocop.search('A1,why does your programming book talk about robocop so much?').group())
