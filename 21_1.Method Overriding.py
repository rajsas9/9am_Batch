'''2 methods with same name with same number of parmeters or arguments 
it is method overriding'''

# Example
########################Error#########################################

class A:  
     
    def show(self):  
         print("In 1 working") 

class B:  
     pass
    
a1=B()

a1.show()
#########################Phone ex#################################
class A:  
     
    def show(self):  
         print("In 1 working") 

class B(A):  
    
    def show(self): 
        print("In 2 working") 
    
a1=B()

a1.show()


