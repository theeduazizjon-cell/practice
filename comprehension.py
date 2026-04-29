"""
Comprehension 
1) What is comprehension & list comp 
2) set and dictionary 
"""

print("=== What is comprehrension & list comp ===")

# Comprehension acts like spread opoerator

"""
Comprehension general syntax: 
a) *iterable 
b) <expression> for item iterable 
c) <expression> for item in iterable <condition> 
"""

# list comp

# a version
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = numbers
print("list_numbers: ", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("----")

# b version
people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]
print("list_people: ", list_people)

# c version

cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

list_cars = [car[0] for car in cars if car[1] > 80]
print("list_cars: ", list_cars)


print("=== Set and Dictionary Comprehensions ===")


# a version
numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}
print("set_numbs: ", set_numbs)

# b version
dict_people = {person[0]: person[1] for person in people}
print("dict_people :", dict_people)

# c version
dict_people = {person[0]: person[1] for person in people if person[1] > 20}
print("dict_people :", dict_people)
