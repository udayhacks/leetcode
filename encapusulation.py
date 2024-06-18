# Python program to
# demonstrate private members
# "__" double underscore represents private attribute. 
# Private attributes start with "__".

# Creating a Base class
class Base:
    def __init__(self):
        self.__a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks" 

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)
