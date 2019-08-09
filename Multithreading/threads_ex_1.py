from threading import *
from time import sleep


class Squares(Thread):
    def run(self):
        for each in range(1, 20):
            print(each ** 2)
            sleep(1)


class Poweroftwo(Thread):
    def run(self, num=5):
        for each in range(1, 20):
            print(num ** each)
            sleep(1)


s1 = Squares()
s2 = Poweroftwo()

s1.start()
sleep(.2)
s2.start()

s1.join()
s2.join()

print('Finished the Execution')

import threading


def coder(number):
    print('Coders:', number)
    return


threads = []
for k in range(5):
    t = threading.Thread(target=coder, args=(k,))
    threads.append(t)
t.start()



