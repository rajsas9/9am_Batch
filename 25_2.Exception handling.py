'''###################Exception Handling###################
Python (interpreter) raises exceptions when it encounter errors
When writing a program, we will encounter errors.
Error caused by not following the proper structure (syntax) of the 
language is called syntax error or parsing error.

Compile time error are ->Syntax error - missing ; or wrong spelling in the statement are syntactical errors
logical error -> code is working fine and 4+4=5 then not correct output
Run time -> division by something. file was missing 
'''

a=5
b=2

print(a/b)

###################User will not understand what the error is#####################################
a=5
b=0

print(a/b)

print("end")
#########################apply try block###############################
'''
Handling an exception
If you have some suspicious code that may raise an exception, you can defend 
your program by placing the suspicious code in a try: block. 
After the try: block, include an except: statement, followed by a block of 
code which handles the problem as elegantly as possible.

try:
   You do your operations here;
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
'''

a=5
b=0

try:
    print(a/b)

except Exception:
     print("U cannot divide the number by zero")

print("end")
##################################################################
a=5
b=2

try:
    print(a/b)

except Exception:
     print("U cannot divide the number by zero")

print("end")
########################### e is objet of exception #####################################
a=5
b=2

try:
    print(a/b)

except Exception as e:
     print("U cannot divide the number by zero", e)

print("end")
#############################################################333
a=5
b=2

try:
    print("Resource open")
    print(a/b)
    print("Resource closed")
except Exception as e:
     print("U cannot diveide the number by zero", e)

print("end")
################################################################
a=5
b=0

try:
    print("Resource open")
    print(a/b)
    print("Resource closed")
except Exception as e:
     print("U cannot divide the number by zero", e)

print("end")
#############################################################
#finally block will be executed if we get error as well as if we don't get the error
a=5
b=0

try:
    print("Resource open")
    print(a/b)
    
except Exception as e:
     print("U cannot diveide the number by zero", e)

finally:
    print("Resource closed")
#########################################################
a=5
b=2

try:
    print("Resource open")
    print(a/b)
    k=int(input("Enter the number"))
    print(k)
except Exception as e:
     print("U cannot diveide the number by zero", e)

finally:
    print("Resource closed")
##########################################################
a=5
b=0


    
try:
    print("Resource open")
    print(a/b)
    k=int(input("Enter the number"))
    print(k)
   
except ZeroDivisionError as e:
     print("U cannot diveide the number by zero", e)

except ValueError as e:
     print("Invalid Input")

except Exception as e:
     print("Something wrong")
     
finally:
    print("Resource closed")


###########################ArithmeticError#################################

try:   
    a = 10/0  
    print (a)
except ArithmeticError:   
        print("This statement is raising an arithmetic exception.")
else:   
    print ("Success.")
    

try:   
    a = 10/2  
    print (a)
except ArithmeticError:   
        print("This statement is raising an arithmetic exception.")
else:   
    print ("Success.")
##############################LookupError#######################################3
a = [1, 2, 3]  
    print (a[5])
    
a = [1, 2, 3]  
print (a[5])
    
try:  
    a = [1, 2, 3]  
    print (a[5])
except LookupError:  
    print ("Index out of bound error.")
else:  
    print ("Success")

try:  
    a = [1, 2, 3]  
    print (a[1])
except LookupError:  
    print ("Index out of bound error.")
else:  
    print ("Success")

############################FILE MISSING ERROR########################################    

import os
os.getcwd()
os.chdir('E:\Office\Python\Rk\PYTHON_master\samplefiles')

ft=open('sample1.txt')
ft=open('sample1.txt','r')

try:
    ft=open('sample1.txt','r')
    ft.write('xyz')
    a=246/0
except IOError:
    print('IO error on file')
except ZeroDivisionError:    
    print('this is wrong division')
else:
    print('this is sucessfully executed')
finally:
    print('this is final statement')

ft.close()
#########################MODULE ERROR####################################
import mat
import math
#############################################################
'''
locals()['__builtins__'] will return a module of built-in exceptions, 
functions, and attributes. dir allows us to list these attributes as strings.
'''
locals()['__builtins__']
print(dir(locals()['__builtins__']))
#############################################