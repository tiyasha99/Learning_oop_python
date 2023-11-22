# First see instance_attributes.py

class MercedesBenz:
    doors = 4
    wheels = 4
    model = 'G'
    """
    Notice the double underscore at the beginning and end of init
    Python reserves this naming convention for methods that implement special behaviour
    These methods are also called DUNDERS (for double underscore)
    Python automatically calls this dunder init after the instance has been created but
    before it is returned to us. So this gives us the oppurtunity to customise 
    those instances
    """
    # Say we want to customise color for each instance
    def __init__(self, color): # This color will be passed when creating the instance
        self.color = color # set the color to the color that is specified

    def drive(self):
        print(f"Mercedez is driving. It is {self}")

# Let's try to create instance without passing a color
"""
m1 = MercedesBenz()
m2 = MercedesBenz()
"""
# TypeError: MercedesBenz.__init__() missing 1 required positional argument: 'color'
# To avoid this we could add a default color like
"""
# def __init__(self, color='red'):
#    self.color = color
"""
# Then MercedesBenz() won't give any error

# So now we need to create instances with a color specified

m1 = MercedesBenz('black')
m2 = MercedesBenz('silver')
print(f"Color of m1:{m1.color}\nColor of m2:{m2.color}")


# CONCEPT CHECK
"""
Why does the above TypeError indicate that only one positional argument is missing?
When in reality there are two in dunder init - self and color

Ans: The reason is that dunder init just like our drive method is bound to the instance.
It is an instance method. Therefore, it will recieve the instance object as the first argument itself
"""


# CONCLUSION

"""
1. Attributes are simply variables associated with objects
2. Instance attributes can be set before and after the isntance attributes is returned
3. That said, it's a best practice to set them in __init__, 
a special method which exists specifically for this purpose
"""



