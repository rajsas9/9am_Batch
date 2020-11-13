'''
A decorator is a design pattern in Python that allows a user to 
add new functionality to an existing object without modifying its structure. 
Decorators are usually called before the definition of a function you want to decorate.

#Parameter to add another function
#Nested function 
#Function return function
#Reference
#Function as parameter
'''
#####################Nested function #####################
def funct1():
    print("function1")
    
def funct2(func):     #func -> reference to the function
    print("function2 call function1")
    func()
    
funct2(funct1)
#####################simple Function return function#####################
def print_str():
    return "Good morning"
    
print(print_str())
#####Func reference#########def decorator func####Changing to upper case####
def str_upper(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner  #calling the function or returning the function 

def print_str():
    return "Good morning"
    
print(print_str())

d=str_upper(print_str)   #use @str_upper instead
print(d())
##############################################################
def str_upper(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

@str_upper
def print_str():
    return "Good morning"
    
print(print_str())









