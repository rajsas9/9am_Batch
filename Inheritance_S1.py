'''
Inheritance is the capability of one class to derive or inherit the properties 
from some another class. The benefits of inheritance are:

--It represents real-world relationships well.
--It provides reusability of a code. We don’t have to write the same code again 
and again. Also, it allows us to add more features to a class without modifying it.
--It is transitive in nature, which means that if class B inherits from another class A, 
then all the subclasses of B would automatically inherit from class A.

1. Single inheritance: When a child class inherits from only one parent class, 
it is called as single inheritance. We saw an example above.

2. Multiple inheritance: When a child class inherits from multiple parent classes, 
it is called as multiple inheritance.

3. Multilevel inheritance: When we have child and grand child relationship.
'''
##################################################################
#Inheritance
class A:  
     
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

a1=A()

a1.feature1()
a1.feature2()
#########################Single level Inhertance##########################
# parent class 
class A:  
     
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

# child class          
class B(A):    # It is child class or subclass -> 
              #Class B is inheriting all the features from class A
       
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4 working")    

# creation of an object variable or an instance          
a1=A()

a1.

# calling a function of the class feature1 using its instance 
a1.feature1()
a1.feature2()

b1=B()

b1.

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
########################Multi level Inheritance#########################
class A:  
     
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    
         
class B(A):    # It is child class or subclass -> 
              #Class B is inheriting all the features from class A
       
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4 working")    

         
class C(B):     
              #Class C is inheriting all the features from A and class B
       
    def feature5(self):  
         print("Feature 5 working") 
                  
c1=C()

c1.

c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

#######################Mutilple ##############################

class A:  
     
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    
         
class B:    #Class B is not inheriting all the features from class A
       
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4 working") 
 
        
class C(A,B):     
              #Class C is inheriting all the features from A and class B
       
    def feature5(self):  
         print("Feature 5 working") 
                  
c1=C()
c1.

b1=B() 


b1.

#######################################################################
#Constructor in Inheritance

class A:  
    def __init__(self):  
        print("In A Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

       
class B(A):  
        
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4  working")    

a1=A()   #A() is a constructor
a1.

a1=B()
#########################################################################
#Constructor in Inheritance
#class A is superclass
class A:  
    def __init__(self):  
        print("In A Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

#class B is subclass       
class B(A): 
    
    def __init__(self):  
        print("In B Init")  
                
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4 working")    

a1=A()   #A() is a constructor
a1=B()

a1.
b1.
 
###########   Super is used############################### 
class A:  
    def __init__(self):  
        print("In A Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

      
class B(A):  
    def __init__(self):  
        print("In B Init")  
    
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4 working")  

a1=B() 

class B(A):  
    def __init__(self):  
        super().__init__()  #Superclass will call both A and B init
        print("In B Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature4(self):  
         print("Feature 4 working")               

a1=B() 

##################################################
class A:  
    def __init__(self):  
        print("In A Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

      
class B:  
    def __init__(self):  
        print("In B Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature4(self):  
         print("Feature 4 working")  
         
class C(A,B):  
    def __init__(self):  
        print("In C Init")           

a1=C() 

########################we are not taking B here########################################

class C(A,B):  
    def __init__(self):  
        super().__init__()
        print("In C Init") 

a1=C() 

#####################Method Resolution Order#######################
#Left to rigt
class A:  
    def __init__(self):  
        print("In A Init")  
    
    def feature1(self):  
         print("Feature 1-A working") 
         
    def feature2(self):  
         print("Feature 2 working")  
         
class B:  
    def __init__(self):  
        print("In B Init")  
    
    def feature1(self):  
         print("Feature 1-B working") 
         
    def feature4(self):  
         print("Feature 4 working")     
         
         
class C(A,B):  
    def __init__(self):  
        super().__init__()
        print("In C Init") 

a1=C() 
a1.feature1()

a.
##################################################################
class A:  
    def __init__(self):  
        print("In A Init")  
    
    def feature1(self):  
         print("Feature 1-A working") 
         
    def feature2(self):  
         print("Feature 2 working")  
         
class B:  
    def __init__(self):  
        print("In B Init")  
    
    def feature1(self):  
         print("Feature 1-B working") 
         
    def feature4(self):  
         print("Feature 4 working")     
         
         
class C(A,B):  
    def __init__(self):  
        super().__init__()
        print("In C Init")
    def feat(self):  
        super().feature2()
        

a1=C() 

       
a1.
a1.feat()

#Python provides us the flexibility to inherit multiple base classes in the child class.

class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  

d = Derived()  

print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  

'''The issubclass(sub, sup) method is used to check the relationships between 
the specified classes. It returns true if the first class is the subclass of 
the second class, and false otherwise.'''
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(issubclass(Derived,Calculation2))  
print(issubclass(Calculation1,Calculation2))  

'''The isinstance() method is used to check the relationship between 
the objects and classes. It returns true if the first parameter, 
i.e., obj is the instance of the second parameter, i.e., class.'''


class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(isinstance(d,Derived))  





