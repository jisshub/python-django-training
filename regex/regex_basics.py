import re


# Passing a string value representing your regular expression to re.compile()
# returns a Regex pattern object.

def isphone_num(text):
    pattern = re.compile(r'\d{3}-\d{3}-\d{3}')
    mobile = re.search(pattern, text)
    return mobile.group()


print(isphone_num('My Phone num is 333-455-232'))

# grouping with paranetheses.

import re


def is_phonenum(text):
    pattern = re.compile(r'(\d{4})-(\d{7})')
    mobile = pattern.search(text)
    whole = mobile.group()
    area = mobile.group(1)
    number = mobile.group(2)
    return whole, area, number


print(is_phonenum('my number is 0484-2617278 '))

