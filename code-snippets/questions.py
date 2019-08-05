# questions 1:
# explanations
# input:
# [1, 2, 3, 4, 5, 6]
# output:
# [4, 5, 6, 1, 2, 3]
# [6,5,2,1,3,4]

import random


def rotate_array(arr):
    random.shuffle(arr)
    return arr


numbers = list(range(17, 24))
shuffled = rotate_array(numbers)
print(shuffled)

# import random

# question 2:
# given a list
# [1,2,3,4,5]
# and a value 6
# retrieve all possible sets of numbers whose sum is 6.
# {2,4}, {1,5}, {4,2}, {5,1}
# [1,2,3,4,5]


sum_list = []


def sum_all(numbers):
    global sum_list
    for each in range(0, len(numbers)):
        for each2 in range(each + 1, len(numbers)):
            if each + each2 is 6:
                sum_list.append({each, each2})
    return sum_list


print(sum_all([1, 2, 3, 4, 5, 6]))

# for i in range(1, 4):
#     for j in range(2, 5):
#         print([i, j])
#         if i + j == 6:
#             print(f"output is, {[i, j]}")
