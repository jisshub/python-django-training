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


# bt it is possible to execute the run() of t1 and run of t2 at the same time.

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
# it shud creates two threads. for instance t1 and t2.
# and t1 will print 'Hello' 4 times and t2 prints 'Hi' 4 times
# bt here it doesnt run as simulataneous
# for eg:
# hello
# hello
# Hi
# hello
# Hi

# this is because even though both class inherits Thread class.
# v r not creating 2 threads here.
# to create 2 threads instead of calling a run mthod, call a start() mthod.


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

# now two threads created for both class.
# bt still it doest executes hello and hi in simultaneous manner.

# Schedulers
# # while v run the program, schedulers which gives a specific time to execute
# and v expect program prints one hello at a given time.
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
