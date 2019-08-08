class Hello:
    def run(self):
        for each in range(4):
            print('hello')


class Hi:
    def run(self):
        for each in range(4):
            print('hi')


t1 = Hello()
t2 = Hi()

t1.run()
t2.run()

# here programs executes in a sequence. ie since v call run() of t1. hello prints. at first
# and later hi prints.


# bt it is possible to execute the run() of t1 and run of t2 simultaneously. ie hello and hi printed one after other.


# by default every execution has one thread.
# and that thread is called MainThread.
# ie our program has one thread called MainThread by default.


# Creating Two Different Threads.
# just use a class called Thread and each class here inherit this Thread class.
# for that v import a module called threading.
# ie here v make diff. threads for both classes.


from threading import *


class Hello(Thread):
    def run(self):
        for each in range(4):
            print('hello')


class Hi(Thread):
    def run(self):
        for each in range(4):
            print('hi')


t1 = Hello()
t2 = Hi()

t1.run()
t2.run()

# when v call the both t1.run() and t2.run(),
# it creates two threads. for instance t1 and t2.
# and t1 will print 'Hello' 4 times and t2 prints 'Hi' 4 times
# bt here it doesnt run as simulataneous
# for eg:
# hello
# hi
# hello
# hi
# hello

# v r creating 2 threads here. bt both depends on the mainthread
# to make both 2 threads independent of mainthread, instead of calling a run mthod, call a start() mthod.
# run() is predefined method of threading module, so if not used run(), threading doesnt work.

from threading import *


# import time


class Hello(Thread):
    def run(self):
        for each in range(10):
            # time.sleep(2)
            print('hello')


class Hi(Thread):
    def run(self):
        for each in range(10):
            # time.sleep(2)
            print('hi')


t1 = Hello()
t2 = Hi()

t1.start()
t2.start()

# now two threads run as independent.
# bt still it doest executes hello and hi in simultaneous manner.

# thread Schedulers
# # while v run the program, thread schedulers which gives a specific time for each thread to execute
# and v expect t1 thread prints one hello at a given time.
# bt schedulers r fast so they prints more no .of hello's at that specific time.
# snce it is going fast, v sleep the scheduler for some seconds.


from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for each in range(10):
            print('hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for each in range(10):
            print('hi')
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
t2.start()

# now hello and hi is executed one after another.
# bt here  hello and hi is collided
# ie these two threads comes at same time to the processer.
# after the sleep they both go to the processor at same time.
# so v set a time in between t1.start() and t2.start().
# thus prevent the collision of two threads.


from threading import *
from time import *


class Hello(Thread):
    def run(self):
        for i in range(20):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for each in range(20):
            print('Hi')
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(.2)
t2.start()

# So here there r total of 3 threads.
#     -- Mainthread
#     -- t1
#     -- t2


# if want to print a statement after the t1 and t2 threads.


from threading import *
from time import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for each in range(5):
            print('Hi')
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(.2)
t2.start()

print('Bye')

# here t1 prints Hello, later t2 prints Hi and Mainthread prints
# Bye.
# bt we want mainthread to execute that statement after finished the exection of
# t1 and t2 thread. ie. at the end.

# so to do that, we ask mainthread to wait until t1 and t2 thread terminates.
# v apply join() method on both threads.


from threading import *
from time import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for each in range(5):
            print('Hi')
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(.2)
t2.start()

t1.join()
t2.join()

print('Bye')

# So here byr is printed since Mainthread waits for t1 and t2 to execute finishng
# and later mainthread is executed.





