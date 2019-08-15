from collections import Counter

count_pair = 0

arr = list()


def sock_merchant(arr):
    global count_pair
    new_arr = Counter(arr)
    for v in new_arr.values():
        # print(v)
        if v % 2 == 0:
            count_pair += 1
    print(count_pair)


size = int(input('Enter Size: '))
while size is not len(arr):
    val = int(input('Value: '))
    arr.append(val)
sock_merchant(arr)
