import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern = re.compile('\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# \d matches all the digits from 0 to 9.

pattern = re.compile(r'\D{3,}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match.group())

# \D matches all the non digits.


pattern = re.compile('\w')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# \w matches all digits and letter including upper case and lower case.

pattern = re.compile('\W')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# \W doesnt matches any digits and letters. it matches other symbols or characters.

pattern = re.compile('\s')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# \s matches spaces indentations, newlines ..

# next we want to match pattern Ha that has a word boundary before it.
# so use \b

pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# # so here, output is like,
# <re.Match object; span=(66, 68), match='Ha'>
# <re.Match object; span=(69, 71), match='Ha'>
# here two Ha has word boundaries before that

# to search for pattern that has no word boudary use \B
pattern = re.compile(r'\BHa')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
    # print(match)

