class MercedesBenz:
    doors = 4
    wheels = 4
    model = 'G'

    def drive(self):
        print(f"Mercedez is driving. It is {self}")


m1 = MercedesBenz()
m2 = MercedesBenz()

print(f"Doors of m1:{m1.doors}\nDoors of m2:{m2.doors}")

# So there are two Mercedes having the same kind of attributes (4 doors, 4 wheels and of model G)
# What if we need to say one is black and the other is silver?

m1.color = 'black'
m2.color = 'silver'

print(f"Color of m1:{m1.color}\nColor of m2:{m2.color}")
# Now we have two different instances with two different values to the same attribute


# But the proper way to do it is to define instances simply at the initialization of instance itself
# This we can do using init. (See instance_attributes_init.py)