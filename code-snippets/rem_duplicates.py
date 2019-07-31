copy = []

i = 0


# count = 0


def remove_duplicates(data1):
    global copy, i
    # for each in data1:
    if data1[i] is data1[i + 1]:
        data1.remove(data1[i + 1])
        i += 1
    return data1


print(remove_duplicates([2, 2, 2, 3, 3, 4]))


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))


