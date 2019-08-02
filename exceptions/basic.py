num = [2, 3, 4]
try:
    num[10]
except Exception as e:
    print(e.args)

finally:
    print('damn')

# when an exceptions occurs in try block,Exception class in except block caught it and print the
# corresponding exception. here it is list index out of range
# finally blk is executed even though exception ocurs or not


tup = (3, 4, 5)
try:
    tup[2] = 10
except Exception as e:
    print(e.args)
finally:
    print('no')

num = [2, 3, 4]
try:
    num.append(4, 5)
except Exception as e:
    # print('cant append a multiple objects to oather list')
    print(e.args)
finally:
    print('hello')
