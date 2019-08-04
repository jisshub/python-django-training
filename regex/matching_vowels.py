# matching all vowels
import re

pattern = re.compile(r'[aeiouAEIOU]')
match = pattern.findall('bharanikulanagara')
print(match)


# matching all consonanats.
import re
regex = re.compile('[^aeiou]')
match = regex.findall('superman')
print(match)
