"""
Array & Set 
1 - Array 
2 - Set 
3 - Specific operators with set 
"""

from array import array
print("==== Array ====")


numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers1:", numbers)

numbers.append(100)
numbers.insert(0, 14)
print("numbers(2):", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(3):", numbers)

del numbers[0:2]
print("numbers(4):", numbers)

print("=== Set ===")
# set of unique collection wihout keeping order!

new_numbers = array("i", [1, 4, 5, 7, 8, 41])
numb_set = set(new_numbers)

print(f"the numbs_set: {numb_set} and type: {type(numb_set)}")

numb_set.add(200)
print("numb_set(2)", numb_set)

numb_set.add(7)
print("numb_set(2):", numb_set)

print("=== Specific operators ===")

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union
result2 = a & b  # intersection
result3 = a - b  # difference
result4 = a ^ b  # symmetric difference

print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)
