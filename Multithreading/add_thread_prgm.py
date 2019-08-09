from threading import *

from time import sleep


class Add(Thread):
    def run(self):
        for i in range(5):
            print(i + 3)
            sleep(2)


class Subtract(Thread):
    def run(self):
        for i in range(5):
            print(i - 3)
            sleep(2)


a1 = Add()
s1 = Subtract()
a1.start()
sleep(.3)
s1.start()


a1.join()
s1.join()

print('hai')
