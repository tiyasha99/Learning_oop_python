"""
Adding state to a class generally means incorporating attributes or properties that
represent the internal data of an object. The state of an object is defined by its attributes, 
and these attributes store information about the object's current condition or configuration.
"""

# For example, lets add two attributes to our class MercedesBenz to increase the state of the class

class MercedesBenz:
    doors = 2
    wheels = 4

# These attributes live in the class namespace
"""
A class namespace in Python refers to the scope 
or context in which names (such as variable names, method names, etc.) 
are defined and can be accessed within a class. Each class has its own namespace, 
which is essentially a dictionary that holds the mapping of names to objects.
"""

# These attributes are accessible under a special dunder dict (dunder is short for double underscore)
# __dict__

print(MercedesBenz.__dict__)
"""
Output: {'__module__': '__main__', 'doors': 2, 'wheels': 4, '__dict__': <attribute '__dict__' 
of 'MercedesBenz' objects>, '__weakref__': <attribute '__weakref__' of 'MercedesBenz' objects>, 
'__doc__': None}
"""

# We can change values defined within the class variables

MercedesBenz.doors = 4
print(MercedesBenz.__dict__)
"""
{'__module__': '__main__', 'doors': 4, 'wheels': 4, '__dict__': <attribute '__dict__' of
 'MercedesBenz' objects>, '__weakref__': <attribute '__weakref__' of 'MercedesBenz' objects>, 
 '__doc__': None}
"""


# We can add new class variables

MercedesBenz.model = 'G'
print(MercedesBenz.__dict__)

"""
{'__module__': '__main__', 'doors': 4, 'wheels': 4, '__dict__': <attribute '__dict__' of 
'MercedesBenz' objects>, '__weakref__': <attribute '__weakref__' of 'MercedesBenz' objects>, 
'__doc__': None, 'model': 'G'}
"""

# By defining the class attributes we have modified the blueprint out of which all instances are created

m3 = MercedesBenz()
m4 = MercedesBenz()

print(m3.doors) # 4
print(m4.doors) # 4
print(m3.model) # 'G'
print(m4.model) # 'G'

# All instances will as expected will follow attributes as their blueprint

"""
1. We traditionally define class state in the class body
2. Class state is stored in mappingproxy object and retrieved using __dict__
3. Class state is shared and accessed by all instances of the class
"""