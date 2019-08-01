import re


def isphone_num(text):
    pattern = re.compile(r'\d{3}-\d{3}-\d{3}')
    mobile = re.search(pattern, text)
    return mobile.group()


print(isphone_num('My Phone num is 333-455-232'))




