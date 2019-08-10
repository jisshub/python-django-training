# The built-in time module allows your Python programs to read the system
# clock for the current time. The time.time() and time.sleep() functions are
# the most useful in the time module.

import time

print(time.time())

# The return value is how many seconds
# have passed between the Unix epoch(12 am
# on January 1, 1970,) and the moment time.time() was
# called.

import time


def Calcproduct():
    for i in range(1000):
        print(i ** 2)


starttime = time.time()
prod = Calcproduct()
endtime = time.time()
print(starttime - endtime)
