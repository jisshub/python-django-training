# matching complicated text patterns might require long, convoluted reg-
# ular expressions.
# verbose mode” can be enabled by passing the variable re.VERBOSE as
# the second argument to re.compile() .

# thus v can specify the regex in multiple line instad of a single long line.


import re

regex = re.compile(r"""

    \d{4}-\d{7}
    -\d{3}-\d{1,2}
    -\d{5}
""", re.VERBOSE)

search_obj = regex.search('0484-2671872-232-01-72392')

print(search_obj.group())



# Example - 2
# matching a filename


import re
regex = re.compile(r"""
    (\w+)
    (\.txt)
""", re.VERBOSE)

match = regex.search('filename.txt')

print(match.group())
