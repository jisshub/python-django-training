# Sometimes you will want to match everything and anything. For example,
# say you want to match the string 'First Name:' , followed by any and all text,
# followed by 'Last Name:' , and then followed by anything again. You can
# use the dot-star (.*)


import re

regex = re.compile(r'firstname: (.*) lastname: (.*)')
match = regex.findall('firstname: jissmon lastname: jose')

print(match)

import re

regex = re.compile('Firstname: (.*) Lastname: (.*)')
match = regex.search('Firstname: jissmon Lastname: jose')
print(match.group(1))
print(match.group(2))

print(match.group())

import re

regex = re.compile(r'.')
match = regex.findall('dfskfds342342$&*&')
print(match)
