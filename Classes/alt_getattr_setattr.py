class MercedesBenz:
    doors = 4
    wheels = 4
    model = 'G'
    
    def __init__(self, color="red"): 
        self.color = color 

    def drive(self):
        print(f"Mercedez is driving. It is {self}")


"""
The python interpretor has a number of functions and types built into it that are always available.
For example, getattr and setattr
"""

# Using getattr we can access attributes of the class

m1 = MercedesBenz('black')
m2 = MercedesBenz()

print(getattr(m1, 'color')) # output: black

# Setting object attributes with setattr

# earlier we would do m2.color = silver but we can also do below

setattr(m2, "color", "silver")
print(m2.color) # Output: silver

"""
Why do we need setaatr or getattr? while m1.color="navyblue" is more straight-forward

This is because for our use case we have 2 objects only. But while writing big codes we might
even have 200 objects. See how these functions are helpful below.
"""

objs = [m1, m2]
attribs = ["color", "doors"]
values = ["navyblue", 3]

for obj in objs:
    for attrib, value in zip(attribs, values):
        setattr(obj, attrib, value)

print(f"M1.COLOR = {m1.color} M2.COLOR = {m2.color}")
print(f"M1.DOOR = {m1.doors} M2.DOOR = {m2.doors}")


"""
NOTE: What is the zip function here?
Zip function returns a zip object. A zip object is an iterable of tuples containining tuples of
each of the sequences passed in. For example:
"""

print(zip(attribs, values)) # <zip object at 0x000002209811F300>
print(list(zip(attribs, values))) # [('color', 'navyblue'), ('doors', 3)

"""
Say we are not using getattr and trying to access an attribute that doesn't exist.

print(m1.wingspan) 
This will immediately give us the below error:
    Traceback (most recent call last):
    ...
    AttributeError: 'MercedesBenz' object has no attribute 'wingspan'
---------------------------------------------------------------------------------------
We can avoid it using try and except but that would just lead to more code.
However, this can be significantly simplified using getattr
"""

# first arg: object
# second arg: attribute
# third arg: default value

print(getattr(m2, "wingspan", "No attribute found")) # Output: No attribute found


"""
1. In addition to the traditional dot access syntax,
 attributes could also be read and set using getattr() and setattr() built-ins

2. These methods are most useful when we're manipulating objects programmatically
and especially so if we are doing so at scale(meaning handling a large number of objects)
"""

