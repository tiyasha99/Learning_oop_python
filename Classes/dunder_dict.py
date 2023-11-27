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
    

m1 = MercedesBenz('lavender')
# Referencing the color attribute on the m1 object
print(m1.color)
# But where is this attribute stored?

"""
All instance attributes are stored in a mapping object that could be assessed using dunder dict
"""

print(m1.__dict__) # OUTPUT: {'color': 'lavender'}

m2 = MercedesBenz('Mint green')

print(m2.__dict__) # OUTPUT: {'color': 'Mint green'}

# NOTE:
# m1 and m2's namespaces are completely different even though they share the same
# MercedesBenz class(or blueprint). To demonstrate this, let's assign a new attribute.


m2.horse_power = 490

print(m2.__dict__) # {'color': 'Mint green', 'horse_power': 490}
print(m1.__dict__) # {'color': 'lavender'}

# We can also assign values  using dunder dict

m1.__dict__["horse_power"] = 290

print(m1.horse_power)