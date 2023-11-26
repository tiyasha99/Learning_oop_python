class MercedesBenz:
    doors = 4
    wheels = 4
    model = 'G'
    
    def __init__(self, color="red"): 
        self.color = color 
        
    def drive(self):
        print(f"Mercedez is driving. It is {self}")

    def autodrive():
        return "Auto-driving for now...."
    
    def create_lease(cls):
        return f"A lease for {cls} is created."
    

    # We can define the builtin decorators as constructors

    create_lease = classmethod(create_lease) # Reference to what we defiined above
    autodrive = staticmethod(autodrive)

    """
    Decorators are more like syntactic sugar. Easier way of defining class and static methods
    than defining them using constructors
    Without the decorators autodrive and create_lease are just instance methods
    Down below we pass the instance method definition to the constructors which 
    changes the instance methods on the fly and converts it to a class/static method.
    And then again we bind that to create_lease/autodrive
    """

m1 = MercedesBenz()
print(m1.autodrive())
print(m1.create_lease())
