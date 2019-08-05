# CASE INSENSITVE MATCHING

import re

regex = re.compile(r'robocop')
match = regex.search('thid is robocop')
print(match.group())
# HERE THE REGEX MATCHED WITH STRING robocop

import re

regex = re.compile(r'robocop')
match = regex.search('thid is ROBOCOP')
print(match.group())

# BT HERE REGEX DOESNT MATCHES AND RETURNS A NONE VALUES SINCE REGEX BY
# DEFAULT CASE SENSITIVE.

# To make your regex case-insen-
# sitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile() .


import re

regex = re.compile(r'superman', re.I)
match = regex.search('best superhero is SUPERman')
print(match.group())


import re

regex = re.compile(r'superman', re.I)
match = regex.search('best superhero is SUPERMAN')
print(match.group())



import re

regex = re.compile(r'SUPERMAN', re.I)
match = regex.search('best superhero is superman')
print(match.group())


# HERE REGEX MATCHES WITH STRING EVN THOUGH THEY HAV DIFFERENT CASES.


