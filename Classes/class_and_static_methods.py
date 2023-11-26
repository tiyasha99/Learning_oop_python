class MercedesBenz:
    doors = 4
    wheels = 4
    model = 'G'
    
    def __init__(self, color="red"): 
        self.color = color 
        
    def drive(self):
        print(f"Mercedez is driving. It is {self}")

    @staticmethod
    def autodrive():
        return "Auto-driving for now...."
    
    @classmethod
    def create_lease(cls):
        return f"A lease for {cls} is created."
"""
    Not all methods defined within the body of the class should necessarily be instance methods
    It is possible to define a method that is static. 
    The way we convert an instance method to a static method is by
    decorating the definition with static method
"""

m1 = MercedesBenz()
m2 = MercedesBenz()

# Functionality is identical regardless of the caller

print(m1.autodrive())
print(m2.autodrive())

"""
Static methods do not have the method signature constraints of instance methods
In fact static methods are just like regular functions.
They just happen to live within the namespace of the class and can therefore be
accessed through the class or any of its instances
"""

# -------------------------------------------------------------------------------------------------------

"""
Class methods are bound to the class and not to its instances
Class methods can be called using the class itself
"""

print(MercedesBenz.create_lease())

# calling through he instance will also work fine
print(m1.create_lease())
