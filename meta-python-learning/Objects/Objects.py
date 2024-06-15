"""
Encapsulation
Abstraction
Polymorphism
Inheritance
"""


# Encapsulation
class Alpha:

    def __init__(self):
        self._a = 2.  # Protected member ‘a’
        self.__b = 2.  # Private member ‘b’


# Polymorphism ------------------.
string = "poly"
num = 7
sequence = [1, 2, 3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)


# Inheritance--------------------->
class Parent:
    #Members of the parent class
    pass


class Child(Parent):
    # Inherited members from parent class
    #  Additional members of the child class
    pass


# Abstraction ==================>
from abc import ABC


class ClassName(ABC):
    pass


# ---------------------- Classes----------
class House:
    """
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    """
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house


house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)


# -------------------------------
class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost


house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)


#-------------------------- Classes --------------
# Sample Solution code
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)


whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")
