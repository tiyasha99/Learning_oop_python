class MercedesBenz:
    pass

print(MercedesBenz) # <class '__main__.MercedesBenz'> (This is an object)
# Even if nothing is defineed within this class - it corresponds to something in memory

print(type(MercedesBenz)) #<class 'type'>

'''
The class that we have defined does not create any instances.
It simply defines the instances that could be created.
A class by default comes with a stae and behaviour.
Basically, by simply defining a class we get an object that encapsulates a number of properties
'''
print(MercedesBenz.__bases__) #(<class 'object'>,)
# Here we get the tuple of base classes
# Right now we get object which is the root object of all classes in Python

# Other attributes
print(MercedesBenz.__name__) # Gives the name of the class MercedesBenz

# A class also has behaviour - so we can call it
print(MercedesBenz()) # <__main__.MercedesBenz object at 0x000001FBBD575C10>

# Above - we get a new instance and we get a memory location for that instance

# Let's define two instances

m1 = MercedesBenz()
m2 = MercedesBenz()
print(f"{m1}\n{m2}")

# Are m1 and m2 instances the same?

print(m1==m2) # False
# By default they are not because they are two different entities in memory
# They are seperate objects just like two identical cars of Mercedes in real world
# These are two objects of the same blueprint


"""
1. A class is a blueprint that represents a type of object
2. Even the simplest class has attributes and behaviour
3. Calling the class creates instances or objects of that class
"""

