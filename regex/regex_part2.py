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
# here two Ha has word boundaries before it.

# to search for pattern that has no word boudary use \B
pattern = re.compile(r'\BHa')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
    # print(match)

# Search and group method
# examples
import re

pattern = re.compile(r'\d{3}\*\d{3}\*\d{3}')
match = pattern.search(text_to_search).group()
print(match)

# here v use search method to seearch for the pattern in the string.
# if not used group() method it returns an regex object,
# so to return actual match we use group().
# here need to use the backslash bfore *


# Example 2
pattern = re.compile(r'\d{3}\.\d{3}\.\d{3,}')
match = pattern.search(text_to_search).group()
print(match)
# here need to use a backslash bfore for each '.'
# then only match is found.


# ^ -caret symbol
# to match the begining of a string.
import re

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'^Start')
match = pattern.search(sentence)
if match:
    print(match)
else:
    print('no match')

# here it prints the match since sentence starts with 'Start'

# below code returns no match since v search for pattern 'sen' which is not the begining of sentence.
import re

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'^sen')
match = pattern.search(sentence)
if match:
    print(match)
else:
    print('no match')

# $ -dollar symbol
# to search for a match at end of the string.
sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'^end$')
match = pattern.findall(sentence)
if match:
    print(match)
else:
    print('no match')


# Checking Vallid data or not
def is_valid_time(date):
    pattern = re.compile(r'^\d{2}:\d{2}$')
    match = pattern.search(date)
    if match:
        return True
    else:
        return False


ans = is_valid_time("22:23")
print(ans)


# Checking valid name or not
def is_valid_name(name):
    pattern = re.compile(r'^[Mr\.|Mrs\.]\D{1,}HOD$')
    match = pattern.search(name)
    if match:
        print(match.group())
        return True
    return False


print(is_valid_name('Mrs.Jissmon Jose, HOD'))

# here v use, [] and place Mr. and Mrs. in it.
# it means name shud start with either one of the following.

# Parsing the Date
import re

date_dict = {}
data_lst = ['d', 'm', 'y']
keys = []
vals = []


def parse_date(date):
    global date_dict, data_lst, keys, vals
    pattern = re.compile(r'^\d{2}[-.,/]\d{2}[-,./]\d{4}$')
    match = pattern.search(date)

    if match:
        match = str(match.group())
        dt_split = re.split(r'\W', match)
        for w in data_lst:
            for n in dt_split:
                for key, val in date_dict.items():
                    keys.append(key)
                    vals.append(val)
                if w not in keys and n not in vals:
                    date_dict.update({w: n})
        return date_dict
    return None


ans = parse_date("12.04.2005")
print(ans)

# Sample Programs

# data = dict(name='jissmon', age='20')
data2 = ['job', 'salary']
data3 = ['asst', 4000]
for i in data2:
    for j in data3:
        print(f"{i}:{j}")
#         data.update({i:j})
# print(data)

data = dict(name='jissmon', age='20')
data2 = ['job', 'salary']
data3 = ['asst', 4000]
keys = []
vals = []
for i in data2:
    for j in data3:
        for key, val in data.items():
            keys.append(key)
            vals.append(val)
        if i not in keys and j not in vals:
            data.update({i: j})
print(data)
