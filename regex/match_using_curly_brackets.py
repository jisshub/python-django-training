# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)


import re

pattern = re.compile(r'\d{3}')
match = pattern.search('43894343')
print(match.group())


import re
regex_obj = re.compile('\w{4,10}')
match = regex_obj.search('fhjfgj458748')
print(match.group())




