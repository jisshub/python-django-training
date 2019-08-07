

# vehicle registration number validation using regular expressions

import re

valid_lst = list()
invalid_lst = list()


def vehicle_valid():
    global valid_lst, invalid_lst
    with open('vehicle_registry.txt', 'r') as veh:
        # print(veh.readlines())
        for each in veh.readlines():
            regex = re.fullmatch(r'^(KL)-\d{2}\s\d{2,4}', each[:-1])
            if regex is None:
                # print('Invalid No')
                # with open()
                invalid_lst.append(each)
            else:
                valid_lst.append(each)
        for each in valid_lst:
            with open('vehicle_no.txt', 'a') as file:
                file.write(each)

        for each in invalid_lst:
            with open('not_veh_no.txt', 'a') as file2:
                file2.write(each)


vehicle_valid()
