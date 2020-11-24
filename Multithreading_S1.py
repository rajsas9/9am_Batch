
class circle:
    def run(self):
        for i in range(5):
            print("cirle")

class square:
    def run(self):
        for i in range(5):
            print("square")


t1=circle()
t2=square()

t1.run()
t2.run()
################ime#######error######################
#To print circle and square if you want to take somet
#Still it is taking only 1 core
#by default you will hve only 1 thread i.e main thread
#Circle should be sub class of thread

class circle(thread):
    def run(self):
        for i in range(5):
            print("cirle")

class square(thread):
    def run(self):
        for i in range(5):
            print("square")


t1=circle()
t2=square()

t1.run()
t2.run()

###################################################
#when you execute circle and square should print simultaneously
from threading import *
#from threading import Thread

class circle(Thread):
    def run(self):
        for i in range(5):
            print("cirle")

class square(Thread):
    def run(self):
        for i in range(5):
            print("square")


t1=circle()
t2=square()

t1.run()
t2.run()

##################################################from threading import *

class circle(Thread):
    def run(self):
        for i in range(50):
            print("cirle")  

class square(Thread):
    def run(self):
        for i in range(50):
            print("square")


t1=circle()
t2=square()

t1.start() # internally it will call run
t2.start()

##################################################from threading import *
# As the av=bove is creating the o/p fast i will make it sleep
# here we are getting both circle and squre at same time or colliding
from time import sleep

class circle(Thread):
    def run(self):
        for i in range(50):
            print("cirle")  
            sleep(1)
            
class square(Thread):
    def run(self):
        for i in range(50):
            print("square")
            sleep(1)
            

t1=circle()
t2=square()

t1.start() # internally it will call run
t2.start()

##################################################from threading import *
# As the av=bove is creating the o/p fast i will make it sleep
# here we are getting both circle and squre at same time or colliding
from time import sleep

class circle(Thread):
    def run(self):
        for i in range(50):
            print("cirle")  
            sleep(1)
            
class square(Thread):
    def run(self):
        for i in range(50):
            print("square")
            sleep(1)
            

t1=circle()
t2=square()

t1.start() # internally it will call run
sleep(0.2)
t2.start()

print("Bye")  # where you will print this
#It is printing in between we want to print the bye at the end

##################################################from threading import *
# As the av=bove is creating the o/p fast i will make it sleep
# here we are getting both circle and squre at same time or colliding
from time import sleep

class circle(Thread):
    def run(self):
        for i in range(5):
            print("cirle")  
            sleep(1)
            
class square(Thread):
    def run(self):
        for i in range(5):
            print("square")
            sleep(1)
            

t1=circle()
t2=square()

t1.start() # internally it will call run
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")  # where you will print this
#It is printing in between we want to print the bye at the end we need to use join





