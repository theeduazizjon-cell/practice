"""
Lists 
1 - working with lists 
2 - list methods 
3 - lambda function
4 - enumerate, map and filter 
"""

print("==== Working with lists ====")
# java/php/ nodejs array -> python lists

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list

for team in groups:
    print(f"the team: {team}")


# constructor
letters = list("Hello World!")
print(f"the letters: {letters} and size: {len(letters)}")

print("-----")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]  # [0, 2]
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("==== List methods ====")

# methods: append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the append result: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert result: {letters}")

size = len(letters) - 1
result = letters.pop(size)  # pop behind
print(f"the pop result: {result} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the pop result2 {result2} and the letters: {letters}")

print("----")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exists:", exist)

animals.clear()
print("animals clear: ", animals)

if "cat" in animals:
    print(f"index of cat", animals.index("cat"))
else:
    print("cat does not exist")

print("-----")
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("numbers:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable sorted

numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")
