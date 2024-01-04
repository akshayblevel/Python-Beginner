from threading import *
from time import sleep


class Read(Thread):
    def run(self):      # run is a method from thread class
        for i in range(5):
            print("Reading text")
            sleep(1)    # Hold thread for one second to observe multiple threads are running


class Write(Thread):
    def run(self):
        for i in range(5):
            print("Writing text")
            sleep(1)


t1 = Read()
t2 = Write()

t1.start()      # start is a method of thread class
sleep(0.2)      # hold for 2 millisecond to avoid collision
t2.start()

# join to wait for main thread to do his job, so "End" will be printed once both the threads job is done
t1.join()
t2.join()

print("End")    # executed on main thread
