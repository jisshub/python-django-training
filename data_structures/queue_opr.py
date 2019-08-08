# Queue Operation

front = 0
rear = -1
q = list()


def add_to_queue(size):
    global rear, front, q
    # if rear > size:
    #     return 'queue is full'
    # else:
    #     rear += 1
    #     print(rear)
    #     q.append(item)
    # return q
    if rear > size:
        return 'Queue Empty'
    while size - 1 > rear:
        item = int(input('Enter an item: '))
        rear += 1
        q.insert(rear, item)

    return q


size = int(input('Size: '))
print(add_to_queue(size))

# Deleting from the Queue


front = 0

numbers = [4, 5, 7, 8]

rear = len(numbers) - 1


def delete_from_q():
    global front, numbers, rear
    if numbers == list():
        return 'queue is empty'
    print(numbers)
    while front <= rear:
        print(f'Removing {numbers[front]} Element from queue')
        numbers.remove(numbers[front])
        print(numbers)
        rear -= 1

    # return numbers


delete_from_q()
