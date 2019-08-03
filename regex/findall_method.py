# findall method returns a list of matches.
import re

pattern = re.compile(r'[a-zA-Z]+')
match = pattern.findall('jissmonjose476@gmail.com')
print(match)

# If there are groups in the regular expression, then findall() will return
# a list of tuples. Each tuple represents a found match, and its items are the
#  matched strings for each group in the regex.

import re

regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
match = regex.findall('hello my numbers is 084-762-2832 and 893-343-3223')
print(match)


