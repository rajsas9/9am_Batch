
print("Hello" + __name__)
'''
import os
os.chdir("E:\Office\Python\Rk\PYTHON_master\Generators")
os.getcwd()
import Generator3

print("Hello Gentleman")
'''
def fib(mymax):
    a,b=0,1
    while True:
        c=a+b
        if c < mymax:
            yield c
            a=b
            b=c
        else:
            break
        
genetator=fib(10) # Generator object is creating

next(genetator)

##############################################
def fib(mymax):
    a,b=0,1
    while True:
        c=a+b
        if c < mymax:
            print('Before yield keyword')
            yield c
            print('After yield keyword')
            a=b
            b=c
        else:
            break
        
genetator=fib(10) # Generator object is creating

next(genetator)
        
    


