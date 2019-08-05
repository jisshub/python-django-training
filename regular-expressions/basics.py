# FINDITER METHOD

# here v generatean iterator object which contains the patterns that matched.
# later iterate over this matches and print its position and also that particular pattern

# import re
#
# count = 0
# match = re.finditer('ha', 'hahhha')
# for each in match:
#     print(each.start())
#     print(each.group())
#     count += 1
#
# print(count)

# Example 2
# import re
#
# count = 0
# x = '[abc]'
# # NEED TO FIND EITHER a, b or c  appears in given string 'ambulance
# match = re.finditer(x, 'ambulance')
# for each in match:
#     print(each.start())
#     print(each.group())
#     count += 1
#
# print(count)

# Example 3
import re

count = 0
x = '[^abc]'
# NEED TO FIND patterns other than a, b or c in the given string 'ambulance
# ^ denotes except
match = re.finditer(x, 'ambulance')
for each in match:
    print(each.start())
    print(each.group())
    count += 1

print(count)

import re

x = '[a-z]'
match = re.finditer(x, 'ambulance8762')
for each in match:
    print(each.group())

import re

x = '[a-zA-Z0-9]'
match = re.finditer(x, 'sadada3423&&&(()')
for each in match:
    print(each.group())

import re

x = '[^a-zA-Z0-9]'
match = re.finditer(x, 'sadada3423&&&(()')
for each in match:
    print(each.group())

# FINDING
import re

x = '\s'
match = re.finditer(x, 'sadada      3423&&&(()')
for each in match:
    print(each.start())

import re

x = '\d'
match = re.finditer(x, 'sadada3423&&&(()')
for each in match:
    print(each.group())

import re

x = '\D'
match = re.finditer(x, 'sadada3423&&&(()')
for each in match:
    print(each.group())

# \w provides any words including digits no special characters.
import re

x = '\w'
match = re.finditer(x, 'sadada3423&&&(()')
for each in match:
    print(each.group())

# \W gives all patterns except words and digits.
import re

x = '\W'
match = re.finditer(x, 'sadada3423&&&(()')
for each in match:
    print(each.group())

# data = ['jiss', 'john', 'kumar']
# import re
#
# re.finditer(data, )
#
# data = []
#
# data.append(4)
#
# print(data)
