import re


def email_validate(email):
    pattern = re.compile(r'^[a-zA-Z]\w+@(gmail|hotmail|yahoo)\.com')
    try:
        match = pattern.search(email)
        return match.group()
    except Exception as err:
        print(err.args)


print(email_validate('jissmon476@.com'))

# pattern = re.compile(r'(Mr\.| Mr\.)\s[a-zA-z]+')
# match = pattern.search('Mr. Jiss')
# print(match.group())
