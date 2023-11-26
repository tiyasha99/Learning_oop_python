"""
1. Define a STudent class with 2 instance attributes (name, age) and 
1 class attribute (eductaional_platform), defaulting to udem

2. Make it so that instances of Student could be creaed by simply specifying the name

3. Define a greet() method which alternates between various name greetings. When invoked,
the method should randomly select a greeting and interpolate in the name of the student.

4. Starting with a list of several student names, create student instances from each, 
and have each student introduce themselves
"""
import random
class Student:
    educational_platform = "udemy"


    def __init__(self, name, age=23):
        self.name = name
        self.age = age
    
    def greeting(self):
        greet_list = ["Hi, I'm", "Hey there, my name is", "Hi. Oh, my name is"]
        n = random.randint(0, len(greet_list) - 1)
        return greet_list[int(n)] + " " + self.name


# s1 = Student('Tiyasha')

# print(s1.greeting())

names = ['Tiyasha', 'Nihal', 'Dev', "Noyna", "Sharon", "Krunal", "Rudo", "Paridhi"]

def create_obj(names):
    return [Student(name) for name in names]


for obj in create_obj(names):
    print(obj.greeting())
