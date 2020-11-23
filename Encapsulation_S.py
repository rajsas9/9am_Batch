# data / method -  Encapsulation/Abstraction /Hide 
'''We can restrict to variables and methods is Encapsulation'''

'''######To prevent the data being modified accidently
Access specifiers - Private and Public
Private methods are not accessable outside the class###############'''

###############how variables can easily be accessed(Public)######################################
class Person:
    def __init__(self, name):
        self.name = name
         
    def display(self):
        print(self.name)
 
person = Person('Dev')
person.display()
#accessing directly from outside
print(person.name)
######################Using Single Underscore#############################
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age
 
    def display(self):
        print(self.name)
        print(self._age)
 
person = Person('Dev', 30)
#accessing using class method
person.display()
#accessing directly from outside
print(person.name)
print(person._age)
#####################Using Double Underscores(Private) - EX1##############
'''
You can observe that variables are still be accessed using methods, 
which is a part of the class. But you cannot access age directly from outside,
as it is a private variable.
'''
class Person:
    def __init__(self):
        self.__chakrasoft()
 
    def display(self):
        print("displaying")
    def __chakrasoftware(self):
        print("Chakra Soft")    

c=Person()
c.display()
c.__chakrasoftware() #private method outside the class

###########################Ex2#######################
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
 
    def display(self):
        print(self.name)
        print(self.__age)
 
person = Person('Dev', 30)
#accessing using class method
person.display()
#accessing directly from outside
print('Trying to access variables from outside the class ')
print(person.name)
print(person.__age)
############Using Getter and Setter methods to access private variables#########
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
 
    def display(self):
        print(self.name)
        print(self.__age)
 
    def getAge(self):
        print(self.__age)
 
    def setAge(self, age):
        self.__age = age
 
person = Person('Dev', 30)
#accessing using class method
person.display()
#changing age using setter
person.setAge(35)
person.getAge()

########################EX1 Protected members#############################

class Car:
    __maxspeed=0
    __name=""
    def __init__(self):
        self.__maxspeed = 900
        self.__name = "supercar"
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    def setspeed(self, speed):
        self.__maxspeed = speed
        print(self.__maxspeed)
ccar = Car()
ccar.drive()
ccar.setspeed(100)

########################EX2  Protected members#############################
#Modify the private variable outside the class and see the result
class Car:
    __maxspeed=0
    __name=""
    def __init__(self):
        self.__maxspeed = 900
        self.__name = "supercar"
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    #def setspeed(self, speed):
        #self.__maxspeed = price
        #print(self.__maxspeed)
ccar = Car()
ccar.drive()
ccar.__maxspeed=100  #Can't modify the variable outside the class
ccar.drive()

########################EX3 Protected members#############################
#We used __init__() method to store the maximum selling price of Computer. 

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

'''
We tried to modify the price. However, we can't change it 
because Python treats the __maxprice as private attributes.
# change the price'''
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
####################################

  