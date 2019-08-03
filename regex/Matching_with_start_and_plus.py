import re

pattern = re.compile('bat(wo)*man')
match = pattern.search('batman')
print(match.group())

# The * (called the star or asterisk) means “match zero or more”—the group
# that precedes the star can occur any number of times in the text. It can be
# completely absent or repeated over and over again.


# Example-2
import re

pattern = re.compile('bat(wo)*man')
match = pattern.search('batwowowowowoman')
print(match.group())

# here group wo occurs many times.

import re

pattern = re.compile('(hi)*\sguys')
match = pattern.search(' guys')
print(match.group())

# here pattern matches the given string even though it dont acontans the 'hi'.


