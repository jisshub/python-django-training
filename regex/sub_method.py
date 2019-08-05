# The sub() method for Regex objects is
# passed two arguments. The first argument is a string to replace any matches.
# The second is the string for the regular expression. The sub() method returns
# a string with the substitutions applied.


import re

regex = re.compile(r'^\d{4}')
replace = regex.sub('0484', '3564-4362492')
print(replace)

# here v create a regex that matches the exact 4 digits at the begining.
# and substitute it with new string '0484'.


import re

regex = re.compile(r'^[a-zA-Z]+\w+')
replace_me = regex.sub('colt374', 'jissmon476@gmail.com')
print(replace_me)

# here v replace username of mail with new one.


import re

regex = re.compile(r'(www).([a-zA-Z]+).([a-z]+)')
match = regex.search('www.amazon.com')
print(match.group(1))
print(match.group(2))
print(match.group(3))

# here v replace dommain name with a new name
import re

regex = re.compile(r'\.[a-zA-Z]+\.')
replace = regex.sub('.flipkart.', 'www.amazon.com')
print(replace)

# print(match.group(2))
# print(match.group(3))
