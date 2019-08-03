# Matching Multiple Groups with the Pipe
#
# The | character is called a pipe. You can use it anywhere you want to match one
# of many expressions. For example, the regular expression r'Batman|Tina Fey'
# will match either 'Batman' or 'Tina Fey' .

import re

pattern = re.compile(r'jiss|jose')
match = pattern.search('jiss and jose')
print(match.group())

# examples
import re

pattern = re.compile(r'batman|ironman|spiderman')
try:
    match = pattern.search('superheroes r the saviuors of the world. is dead now who?')
    print(match.group())
except Exception as e:
    print(e.args)
finally:
    print(pattern)

# You can also use the pipe to match one of several patterns as part of
# your regex. For example, say you wanted to match any of the strings 'superman' ,
# 'superwomen' , 'supergirl' , and 'superboy' . Since all these strings start with super , it
# would be nice if you could specify that prefix only once. This can be done
# with parentheses.


import re

pattern = re.compile(r'super(man|women|girl|boy)')
match = pattern.search('superboy')
match = match.group()
# print(match)
try:
    with open('super2.txt', 'w') as file_to:
        file_to.write(match)
    with open('super2.txt', 'r') as file_to_rd:
        print(file_to_rd.read(), end='')

except Exception as err:
    print(err.args)

