#!/usr/bin/env python3
import re
nameRegex = re.compile(r'FirstName: (.*) Last Name: (.*)')
mo = nameRegex.search('FirstName: A1 Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
