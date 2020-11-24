
######################Without creating a class#########################
from threading import *
print(current_thread().getName())
def mt():
    print("Child Thread")
child=Thread(target=mt)
child.start()
print("Executing thread name :",current_thread().getName())
######################By extending the Thread class:#########################
'''
When a child class is created by extending the Thread class, the child class 
represents that a new thread is executing some task. When extending the 
Thread class, the child class can override only two methods i.e. the __init__() 
method and the run() method
'''
import threading
import time
class mythread(threading.Thread):
    def run(self):
        for x in range(7):
            print("Hi from child")
a = mythread()
a.start()
a.join() #join() function, which makes the main thread wait for the child to finish.
print("Bye from",current_thread().getName())

######################Without creating a class#########################
from threading import *
class ex:
    def myfunc(self): #self necessary as first parameter in a class func
        for x in range(7):
            print("Child")
myobj=ex()
thread1=Thread(target=myobj.myfunc)
thread1.start()
thread1.join()
print("done")
##################without thread###########################
import time
def sqr(n):
    for x in n:
        time.sleep(1)
        x%2
def cube(n):
    for x in n:
        time.sleep(1)
        x%3
n=[1,2,3,4,5,6,7,8]
s=time.time()
sqr(n)
cube(n)
e=time.time()
print(e-s)
#####################With Threads######################
import threading
from threading import *
import time
def sqr(n):
    for x in n:
        time.sleep(1)
        print('Remainder after dividing by 2',x%2)
def cube(n):
    for x in n:
        time.sleep(1)
        print('Remainder after dividing by 3',x%3)
n=[1,2,3,4,5,6,7,8]
start=time.time()
t1=Thread(target=sqr,args=(n,))
t2=Thread(target=cube,args=(n,))
t1.start()
time.sleep(1)
t2.start()
t1.join()
t2.join()
end=time.time()
print(end-start)
###########################

