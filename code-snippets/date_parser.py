
# Date Parsing Program
import re

date_dict = {}
data_lst = ['d', 'm', 'y']
keys = []
vals = []


def parse_date(date):
    global date_dict, data_lst, keys, vals
    pattern = re.compile(r'^\d{2}[-.,/]\d{2}[-,./]\d{4}$')
    match = pattern.search(date)

    if match:
        match = str(match.group())
        dt_split = re.split(r'\W', match)
        for w in data_lst:
            for n in dt_split:
                for key, val in date_dict.items():
                    keys.append(key)
                    vals.append(val)
                if w not in keys and n not in vals:
                    date_dict.update({w: n})
        return date_dict
    return None


ans = parse_date("12.04.2005")
print(ans)
