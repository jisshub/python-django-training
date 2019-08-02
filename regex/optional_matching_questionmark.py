import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo1 = batRegex.search('The adventures of Batwoman')
print(mo1.group())

#
#
# The (wo)? part of the regular expression means that the pattern wo is
# an optional group. The regex will match text that has zero instances or
# one instance of wo in it. This is why the regex matches both 'Batwoman' and
# 'Batman' .