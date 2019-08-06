import re


def match_it(name):
    regex = re.fullmatch('[a-k][369][a-zA-Z#]', name)

    if regex is None:
        return 'invalid'
    else:
        return 'valid'


name = input('Enter name: ')
print(match_it(name))

import re


def match_it(name):
    regex = re.fullmatch('[a-k][369][a-zA-Z#]+', name)

    if regex is None:
        return 'invalid'
    else:
        return 'valid'


name = input('Enter name: ')
print(match_it(name))
