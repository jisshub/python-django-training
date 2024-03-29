# multitasking -- Performing multiple tasks at a time.
# multitasking is achived thru multithreading and multiprocessing.


# to do threading in python

# import module threading.

# here v import all the functions of threading module.

from threading import *

print(current_thread().getName())

# MainThread is to control the flow of program

# ceating thread with out using calss

from threading import *


def display():
    for i in range(5):
        print('helo')
    print(current_thread().getName())


for i in range(5):
    print('helo hai')
print(current_thread().getName())

display()

# here the for loop outside the display() is executed first, later function is called and
# then loop inside it executes.


# here there is just one thread, ie. MainThread.

from threading import *


def display():
    for i in range(5):
        print('Child Thread')

    print(current_thread().getName())


# create a thread class
t = Thread(target=display)

for i in range(5):
    print('Main Thread')
print(current_thread().getName())

t.start()

# here both the part of the program is indepenedent.
# while v run the program, thread scheduler decides and assign the task to any one of thread.
# so the result will be shuffled.

# here Thread is a class and v assign parameter target to it .
# t is an object.

# THre r several thread scheduing algorithms.
#   --Round Robin Scheduling alg.
#         --here  v assign a time stamp for each thread.


# creating thread by inherting the Thread class.

from threading import *


class Mythread(Thread):
    def run(self):
        for each in range(3):
            print('thread')


t = Mythread()
t.run()

for each in range(4):
    print('mainthread')

# here n above program threading doesnt happern since v dont call start method..
# it simply calls the run method of Mythread.

# using start method.

from threading import *


class Mythread(Thread):
    def run(self):
        for each in range(3):
            print('thread')


t = Mythread()
t.start()
# t.run()
for each in range(4):
    print('mainthread')

# Example

import time
from threading import *


class Test:
    def m1(self):
        for each in range(3):
            time.sleep(3)
            print('thread')


obj = Test()
# obj.m1()
t = Thread(target=obj.m1())
t.start()

for each in range(5):
    print('hai')

# here the child  exectes first, since v specify the obj.m1() as an argument to parameter target.
# so here no threading occurs.


# Examplee
import time
from threading import *


class Test:
    def m1(self):
        for each in range(3):
            print('thread')
            sleep(2)


obj = Test()
# obj.m1()
t = Thread(target=obj.m1)
t.start()

for each in range(5):
    print('hai')

# here v specify obj.m1 instead of obj.m1() as argument to target parameter.


# Example_4

from threading import *
from time import sleep


def doubles(numbers):
    for i in numbers:
        sleep(2)
        print('doubles', i ** 2)


def squares(numbers):
    for n in numbers:
        sleep(2)
        print('square', n * n)


numbers = [2, 3, 4]
# bgntime = time.time()
t1 = Thread(target=doubles, args=(numbers,))
t2 = Thread(target=squares, args=(numbers,))
t1.start()
sleep(.3)
t2.start()
# if v just

t1.join()
t2.join()

print('hello')

##############################################################################


from threading import *
from time import sleep


class Doubles(Thread):

    def run(self):
        numbers = [2, 3, 5]
        for i in numbers:
            sleep(2)
            print('doubles', i ** 2)


class Squares(Thread):
    def run(self):
        numbers = [2, 3, 5]
        for n in numbers:
            sleep(2)
            print('square', n * n)


t1 = Doubles()
t2 = Squares()
# numbers = [2, 3, 4]

t1.start()
sleep(.3)
t2.start()
# if v just

t1.join()
t2.join()

print('hello')

#################################################################33

from threading import *
from time import sleep


def divisible():
    for each in range(1, 20):
        if each % 3 is 0:
            print(f"{each} divisble by 3")
            sleep(2)


def divisibleby5():
    for each in range(1, 20):
        if each % 5 is 0:
            print(f"{each} is divisble by 5")
            sleep(2)


t1 = Thread(target=divisible)
t2 = Thread(target=divisibleby5)

# divisible()
t1.start()
sleep(.4)
t2.start()
