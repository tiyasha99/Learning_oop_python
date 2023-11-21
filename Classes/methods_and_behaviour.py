class MercedesBenz:
    doors = 4
    wheels = 4
    model = 'G'
    # At this point the class only has state - no behaviour or actions

    # To add behaviour to a class, we simply define a function within its body
    """
    This method is called an instance method as it is part of the body of the class
    Instance methods always take self as first param
    "self" is called self by convention
    It can be called anything else
    """
    
    def drive(self):
        # return "A car is being driven"
        return self # <__main__.MercedesBenz object at 0x00000268CA185CD0> - 
                    # representation of the m1 instance
    


# Now let us create an instance of the class
m1 = MercedesBenz()
print(m1.drive())
print(m1 == m1.drive()) # when we are returning self we can simply say that the drive method is 
                        # returning the instance itself (Output: True)

# is m1.drive() = MercedesBenx?
print(m1.drive() == MercedesBenz) # False - self is not the blueprint. It is not the class. 
                                  # It is simply the instance itself



class Audi:
    doors = 4
    wheels = 4
    model = 'G'
    def drive(self):
        return f"An Audi is being driven and it is {self}"
    

a1 = Audi()
a2 = Audi()

print(f"self returns the instances itself and since"
      f" a1 and a2 are two different instances this will be false- {a1.drive() == a2.drive()}")


print(f"Audi.drive is {Audi.drive}. It is a {type(Audi.drive)}")
# But when we look at it from an instance perspective

print(f"It becomes a bound method of a very specific object like a1 - {a1.drive}")


"""
1. We add behaviour to our classes by defining functions
2. These functions are special in that they always have atleast one parameter (self)
3. That parameter by convention is called self
4. When functions are defined within the body of a class, they become bound or attached to the instances
of that class
"""