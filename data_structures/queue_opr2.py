# Using List as queues

# It is also possible to use a list as a queue, where the first element added is the first element retrieved
# (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the
# end of list are fast, doing inserts or pops from the
# beginning of a list is slow (because all of the other elements have to be shifted by one).

# eg:
# data.pop(0)   -- to pop an element from the front of list, need to pass the index.
# data.insert(0, object) -- to insert an element to the front of list, need to pass the index.

# >>> data = [4,5,6]
# >>> data.insert(0, 10)
# >>> data
# [10, 4, 5, 6]
# here when v insert 10 at first index, all other element were shifted by one.


# so here v not use the lists.

# To implement a queue, use collections.deque which was designed to have
# fast appends and pops from both ends. For example:

from collections import deque

queue = deque(['Eric', 'Sule', 'Rodrygo'])
print(queue)
print(type(queue))

# now queue is a deque object, not a list object.
# deque object has methods similar to list
# use append mthod of deque to add item to queue.

queue.append('Terry')
queue.append('Graham')
print(queue)
# new elements appended to the end of the queue.

# Next to remove the items from the front of the queue.
# use popleft() method of deque
# which pops the items from the left of the queue(ie. front).

queue.popleft()
print(queue)

# again pop from the left of the queue
queue.popleft()
print(queue)


# Appending to the left/front of the queue.
# use appendleft() method.
queue.appendleft('Watson')
print(queue)
