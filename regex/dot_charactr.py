import re

regex = re.compile(r'.')
match = regex.findall('dfs\nkfds342342$&*&\n')
print(match)

# dot character matches any thing except new line \n.

