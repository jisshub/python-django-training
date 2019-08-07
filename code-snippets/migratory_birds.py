i = 0
# j = 0
types = list()
count_lst = list()

key_lst = list()
val_lst = list()


# count_val = dict()


def migratory_birds(size):
    global i, types, count_lst, key_lst, val_lst
    while size > i:
        bird_type = int(input('Enter type: '))
        i += 1
        types.append(bird_type)
    # return types
    for j in range(len(types)):
        c = types.count(types[j])
        count_lst.append(c)
    # convert types and count_lst lists to a dictionary. so use zip() method
    count_val = dict(zip(types, count_lst))
    # in count_val dictionary, each number in types list woud b key and each number in count_lst woud be values.
    # return count_val
    for keys, values in count_val.items():
        # print(key, value)
        val_lst.append(values)
        key_lst.append(keys)
    print(key_lst, val_lst)
    # if set(val_lst)
    # check whther duplicates in list
    if len(val_lst) != len(set(val_lst)):
        ind = val_lst.index(max(val_lst))
        max_type = key_lst[ind]

    return f"maximum type is {max_type}"


print(migratory_birds(5))
