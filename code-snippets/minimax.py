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
        numbers.insert(e, len(numbers))
        i += 1
        # j += 1


minimax([1, 2, 4, 5])


class Humans:
    # def__init__()
    def __init__(self, height):
        # self.name = name
        self.height = height

    def __add__(self, other):
        self.height += other.height
        return Humans(self.height)

    def __repr__(self):
        return str(self.height)


h1 = Humans(33)
h2 = Humans(12)
h3 = Humans(11)
add = h1 + h2 + h3
print(add)



# class