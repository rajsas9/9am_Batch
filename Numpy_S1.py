# Python program to demonstrate  
# basic array characteristics 
'''
Numpy - Numerical Python
numpy vs list
numpy operators
numpy functions
#Numpy is the core library for Scientific computing in Python
#It provides a high performance multidimentional array object, and tools for working 
with these arrays
n dimensional array object
linear Algebra
multidimentional container for data(2d or 3d(like cube))
randon number capabilities

6 types of arrays
array()
linspace()
logspace()
arange()
zeros()
ones()
'''

#########################error as array does not support##################################
#It will not support multidimentional array
from array import *

arr = array('i',[1,2,3],[4,5,6])

print(arr)
###################error#########################
from numpy import *

arr = array('i',[1,2,3],[4,5,6])  #no need to mention i

print(arr)
########################No need to mention the type####################
from numpy import *
arr = array([1,2,3,4,5,6])
print(arr)

arr = array([1,2,3,4,5,6],int)
print(arr)
print(arr.dtype) #It give the type of array

#############################float#######################
from numpy import *

arr = array([1,2,3,4,5,6.0])
arr = array([1,2,3,4,5,6.0],float)

print(arr)
print(arr.dtype) #It give the type of array
#All the values should be of same type
#here all the values are converted to float
####################################################
from numpy import *

arr = linspace(0,15,10) #start stop step

print(arr)
print(arr.dtype) #It give the type of array
#breaks into 10 different parts with float


arr = linspace(0,15) #start stop 

print(arr)
print(arr.dtype) 
#by default it give 50 parts
####################################################
arr = arange(1,15,2) # first,last,steps

print(arr)
#skip 2 numbers
####################################################

arr = logspace(1,20,5) # first,last,steps

print(arr)   #check the first number and last number in range
#all the numbers are b/w , space depends on 5 
#######################################

arr = logspace(1,20,5) # first,last,steps

print(arr)
print('%.2f' %arr[0]) #.2 for 2decimals
print('%.2f' %arr[4]) # you can change the value here
                        # five parts

#10 raise to 1 and 10 raise to 20 and all other numbers are in b/w
####################################################
arr = zeros(4) # giving float   size 4
print(arr)   #gives all the numbers as zero
####################################################
arr = ones(4) # giving float
arr = ones(4,int)
print(arr)   # It gives you ones
####################ADD###################################
arr = array([1,2,3,4,5])

arr=arr+5

print(arr)
######################################################
arr1 = array([1,2,3,4,5])
arr2 = array([5,6,8,4,2])

arr3=arr1+arr2
print(arr3)
######################################################
arr = array([1,2,3,4,5])

print(sin(arr))
print(tan(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))

######################################################
arr1 = array([1,2,3,4,5])
arr2 = array([5,6,8,4,2])

print(concatenate([arr1,arr2]))
####################copy##################################
arr1 = array([1,2,3,4,5])

arr2=arr1
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
################################################
arr1 = array([1,2,3,4,5])

arr2=arr1.view()  #nhelp you to create a different --here the address is different location
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
##################shallow copy##############################

arr1 = array([1,2,3,4,5])      #copy the elements  if you change the value 26813

arr2=arr1.view()
arr1[1]=7
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
##################deep copy##############################

arr1 = array([1,2,3,4,5]) #changes are reflected in first arry not on the second

arr2=arr1.copy()
arr1[1]=7
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
#######################Two Dimentional array################################
arr1 = array([
               [1,2,3],
               [4,5,6]
            ])
print(arr1.shape)  # It give 2 rows and 3 columns

print(arr1.size) 

#####################2D array to 1D array######################################
arr1 = array([
               [1,2,3],
               [4,5,6]
            ])

arr2=arr1.flatten()
print(arr2)
##################### 1D array to 2D array ######################################
arr1 = array([
               [1,2,3,6,2,9],
               [4,5,6,7,11,12]
            ])

arr2=arr1.flatten()
arr3=arr2.reshape(3,4) 
arr4=arr2.reshape(2,2,3)  #2 rows , 2 rows and 3 columns
print(arr4)
###############################Matrices#####################################
# Metrices are dimentional arrays
arr1 = array([
               [1,2,3,6],
               [4,5,6,7]
            ])

m=matrix(arr1)
print(m)
###########################################
m=matrix('1,2,3;6,4,5;7,8,9')
print(m)
######################print diagnal#####################
m=matrix('1,2,3;6,4,5;7,8,9')
print(diagonal(m))
print(m.max())
###################################################
m1=matrix('1,2,3;6,4,5;7,8,9')
m2=matrix('1,2,3;7,4,2;5,9,6')

m3=m1*m2

print(m3)
#######################################################






























