
# Matching Multiple Groups with the Pipe
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
