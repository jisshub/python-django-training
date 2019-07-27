hg_lst = []
count = 0


def birthday_cakes(n):
    global hg_lst, count
    limit = 0
    while limit < n:
        height = int(input('Enter height: '))
        hg_lst.append(height)
        limit += 1
    # print(hg_lst)
    max_element = max(hg_lst)
    hg_lst.remove(max_element)
    count += 1
    while max_element in hg_lst:
        hg_lst.remove(max_element)
        count += 1
    return count


size = int(input('Enter size: '))
print(birthday_cakes(size))
