'''
A Python generator is a function which returns a generator iterator 
(just an object we can iterate over) by calling yield . yield may be called with a value, 
in which case that value is treated as the "generated" value.

Single value Iter or one by one value and we need to define func like iter n next,
If list of values then genertors 
Genertors gives u itertors


Differences between Generator function and Normal function
Here is how a generator function differs from a normal function.

Generator function contains one or more yield statements.
When called, it returns an object (iterator) but does not start execution immediately.
Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
Once the function yields, the function is paused and the control is transferred to the caller.
Local variables and their states are remembered between successive calls.
Finally, when the function terminates, StopIteration is raised automatically on further calls.
'''
'''#########################Generator##############################''' 
def G1(): 
   
    yield 3 #special keyword which will make func as generator
  
values=G1()
print(values) 
#########################################################
def G1(): 
   
    return 3
  
samp=G1()
print(samp) 
#########################################################
def G1(): 
   
    yield 3
  
samp=G1()
print(samp.__next__()) 

#####################################################
def G1(): 
   
    yield 2
    yield 3
    yield 4
    yield 5
  
samp=G1()
print(samp.__next__()) 

def G1(): 
   
    yield 2
    yield 3
    yield 4
    yield 5
  
samp=G1()
print(samp.__next__()) 
print(samp.__next__()) 

for i in samp: 
    print(i)
############################################################

def G1(): 
   
    n=1
    
    while n< 10:
        sq=n*n
        yield sq
        n+=1
samp=G1()
print(samp.__next__()) 
print(samp.__next__()) 

for i in samp: 
    print(i)
############################################################









