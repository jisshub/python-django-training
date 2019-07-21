# Regular  Expressions

# # import re

# raw string: a string that is prefixed with r
# eg:

print('\tdata')
# when v run the above code ,python replaces the \t with an actual tab space.

print(r'\tdata')
# when v run this code python treats the \t as a string and not a tab space.

# Example 1

# to input the pattern to search for, v use re.compile
# to search for that pattern in the text, v use findall method. also there r methods to do it also.
import re

sentence = 'Start a sentence and then bring it to the end sen'
pattern = re.compile('sen')
match = pattern.findall(sentence)
print(match)

# here v find a pattern 'a' from the 'sentence'.
# Note: findall method returns a list as the result
# in case pattern doesnt have match it returns an empty list


sentence = 'Start a sentence and then bring it to the end'
pattern = re.compile('sen')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)

# here v use finditer() to find match that matches with the pattern
# and output looks like below:
# <re.Match object; span=(8, 11), match='sen'>
# here span=(8,11) means
# match is from index 8 to index 11
# can prove it by slicing the string
#  print(sentence[8:11]


# matching a url

url = 'Traversymedia.com'
pattern = re.compile('Traversymedia\.com')
match = pattern.findall(url)
print(match)

# matching a email id
email = 'jissmon@gmail.com'
pattern = re.compile('jissmon@gmail\.com')
# match = pattern.findall(email)
# print(match)

matches = pattern.finditer(email)
for match in matches:
    print(match)
