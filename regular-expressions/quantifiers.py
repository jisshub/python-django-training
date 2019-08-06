# Quantifiers


# '+' - matches muliple occurneces of letter a in the string.
import re

match = re.finditer('a+', 'aabeaaasdgsaa')
for each in match:
    print(each.group())

import re

match = re.finditer('a*', 'aabeaaasdgsaa')
for each in match:
    print(each.group())
    print(each.start())
# matches any no. a of including zero ocuurences of a



import re

match = re.finditer('a?', 'aabeaaasdgsaa')
for each in match:
    print(each.group())
    print(each.start())

# matches a indiviusally intead of group

import re

match = re.finditer('a{2}', 'aabeaaasdgsaa')
for each in match:
    print(each.group())

# matches exactly 2 occurences of a.

import re

match = re.finditer('a{2,5}', 'aabeaaasdgsaaaaaaa')
for each in match:
    print(each.group())

# matches minimum 2 occurence of a and maximum 5 occurence of a.
# matches excalty with in that range.


import re

match = re.finditer('^a', 'beaaasdgsaa')
for each in match:
    print(each.group())


# checks whether the string starts with 'a'.




import re

match = re.finditer('a$', 'aabeaaasdgsaa')
for each in match:
    print(each.group())

import re

match = re.fullmatch('a', 'dakdhsk')




