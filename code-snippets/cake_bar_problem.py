i = 0
array = []


def chocolate_bar():
    count = 0
    global array, month, day
    if month is 2 and day is 3:
        for i in range(0, len(array)):
            for j in range(1, len(array)):
                if array[i] + array[j] == day:
                    count += 1
        return count


limit = int(input('Enter Squares: '))
while i < limit:
    s = int(input('Enter number: '))
    array.append(s)
    i += 1

month = int(input('Enter Month: '))
day = int(input('Enter day: '))
print(chocolate_bar())
