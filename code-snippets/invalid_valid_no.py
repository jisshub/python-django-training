import re


def find_phone():
    file = open('phone_num.txt', 'r')
    new = file.readlines()
    for each in new:
        print(each[:-1])
        regex = re.fullmatch('^[6-9]\d\d{4}', each[:-1])
        if regex is None:
            print(f"{each[:-1]} is invalid")
            f = open('invalid2.txt', 'a')
            f.write(each)
        else:
            print(f"{each[:-1]} is valid")
            f1 = open('valid.txt', 'a')
            f1.write(each)
    # file = open('valid.txt', 'r')
    # print(file.read())
    # file2 = open('invalid.txt', 'r')
    # print(file2.read())


find_phone()
