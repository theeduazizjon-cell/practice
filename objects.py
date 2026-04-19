"""
Objects 
1 - What is object 
2 - Iterable objects and Range 
3 - Dictionary 
4 - Error handling system 
"""

import array  # package/module
import math  # package/module

from math import ceil, asin  # another way to iniate the package/module

print("=== what is object ===")
# An object is special data type that has got its own state and method properties
# Everything is an object in Python

print(type("Hello World"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional programming & OOP
# OOP 4 concepts: Abstraction, Encapsulation, Inheritance and Polymorphism
result1 = math.ceil(97.7)  # call
print("result:", result1)

result2 = ceil(98.7)
print("result2:", result2)


print("=== Error handling ===")
car_dict = dict(name="toyota", year=2026, electric=True)
try:
    print("passed here")
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
else:
    print("Executed succesfully without errors")
finally:
    print("Final closing logic")
