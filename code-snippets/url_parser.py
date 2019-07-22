url = 'https://blog.hubspot.com/marketing'
# print(url)

import re

url_2 = []
url_info = ['Scheme', 'Subdomain', 'Second-level domain', 'top-level domain', 'subdirectory']
url_dict = {}
keys = []
values = []


def parse_url(url):
    global url_2, url_info, url_dict, keys, values
    new_url = re.split(r'\W', url)
    # return new_url
    for each in new_url:
        if each is '':
            new_url.remove('')
        else:
            url_2.append(each)
    # print(url_2)
    for each in url_info:
        for each2 in url_2:
            for k, v in url_dict.items():
                keys.append(k)
                values.append(v)
            if each not in keys and each2 not in values:
                url_dict.update({each: each2})
    return url_dict


print(parse_url(url))
















