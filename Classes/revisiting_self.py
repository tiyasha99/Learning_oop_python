class MercedesBenz:
    doors = 4
    wheels = 4
    model = 'G'
    
    def __init__(self, color="red"): 
        self.color = color 
    # self represents the object itself of the class
    def drive(self):
        print(f"Mercedez is driving. It is {self}")

    """
    When we define methods within the class body, python, by default assumes that,
    they are instance methods and binds then in such a way that the first argument 
    these methods receive is always the instance itself.
    """
    # This is syntactically correct. Hence no error will be thrown
    def auto_drive():
        return "Auto-driving for now...."
    

m1 = MercedesBenz()

# TypeError will come for below
print(m1.auto_drive())