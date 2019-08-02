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
