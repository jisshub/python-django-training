sum(list(range(2, 10)))


# empty = []


def minimax(numbers):
    global e
    i = 0
    # j = 0

    while i < len(numbers):
        # empty.append(numbers[i])
        # i += 1
        e = numbers.pop(i)
        print(sum(numbers))
        numbers.insert(e, 0)
        i += 1
        # j += 1


minimax([1, 2, 4, 5])
