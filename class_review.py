# Review how a class is constructed and how variables are initialized
class Person:
    # Class initializer
    def __init__(self, name, age):
        # self needs to be used when declaring the variable, so that
        # each instance has its own copy of that variable
        self.person_name = name
        # Can use double underscores to make this variable private
        self.person_age = age

    # Creating methods for the class 
    def birthday(self):
        self.person_age += 1

    def getName(self):
        return self.person_name

# After declaring the class, we actually implement 
# the declaration and methods here

bob = Person('Bob', 32)
print(bob.getName())
# prints Bob

bob.birthday()
print(bob.person_age)
# prints 33