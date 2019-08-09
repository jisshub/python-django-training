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

##############################################################################################

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

########################################################################################################


from threading import *
from time import sleep


class Divisor:
    def divisible(self):
        for each in range(1, 20):
            if each % 3 is 0:
                print(f"{each} divisble by 3")
                sleep(2)

    def divisibleby5(self):
        for each in range(1, 20):
            if each % 5 is 0:
                print(f"{each} is divisble by 5")
                sleep(2)


obj1 = Divisor()

t1 = Thread(target=obj1.divisible)
t2 = Thread(target=obj1.divisibleby5)

# divisible()
t1.start()
sleep(.4)
t2.start()
