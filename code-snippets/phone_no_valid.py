# Phone number Validation
import re


def phone_num(phone):
    regex = re.fullmatch('^[6-9]\d\d{5}', phone)

    if regex is None:
        return 'Invalid Phone'
    else:
        return 'Valid Number'


number = input('Enter Phone: ')
print(phone_num(number))
