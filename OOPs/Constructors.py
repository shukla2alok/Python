class Animal:
    def __init__(self, name):
        self.name = name
    # Multiple constructors
    # This constructor will override the previous constructor
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def display(self):
        print("Name:", self.name)
        print("Species:", self.species)

# Creating object
animal = Animal("Dog")  # This will throw an error that __init__() missing 1 required positional argument: 'species'
animal.display()

# Hack to create multiple constructors
# We can create multiple constructors by checking the number of parameters
# and then assigning the values to the attributes of the object.


class MyClass:
    def __init__(self, param1=None, param2=None):
        if param1 is not None and param2 is not None:
            # Constructor with two parameters
            self.param1 = param1
            self.param2 = param2
        elif param1 is not None:
            # Constructor with one parameter
            self.param1 = param1
            self.param2 = None
        else:
            # Default constructor
            self.param1 = None
            self.param2 = None

# Creating objects using different constructors
obj1 = MyClass()
obj2 = MyClass("Value 1")
obj3 = MyClass("Value 1", "Value 2")

# Displaying the values of the object
print(obj1.param1, obj1.param2)
print(obj2.param1, obj2.param2)
print(obj3.param1, obj3.param2)

# This is not a recommended way to create multiple constructors as it makes the code complex.
# The recommended way is to use default values for the parameters of the constructor.

# Default values for constructor parameters
# We can set default values for the parameters of the constructor.
# If the value of a parameter is not provided while creating an object, then the default value will be used.
# This way, we can create multiple constructors with different parameters.

class MyClass:
    def __init__(self, param1=None, param2=None):
        self.param1 = param1
        self.param2 = param2

# Creating objects using different constructors
obj1 = MyClass()
obj2 = MyClass("Value 1")
obj3 = MyClass("Value 1", "Value 2")

# Displaying the values of the object
print(obj1.param1, obj1.param2)
print(obj2.param1, obj2.param2)
print(obj3.param1, obj3.param2)
