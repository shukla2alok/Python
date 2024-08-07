# class
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

# Create object
person1 = Person("John", 36)
# Call method
person1.myfunc()

person2 = Person("Alice", 25)
person2.myfunc()