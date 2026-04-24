"""
Loop operators 
1 - for 
2 - break/else 
3 - while 
"""

print("==== for operator =====")
text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)  # [0, 5)

for letter in text:
    print(f"the letter: {letter}")

print("-----")

for number in numbs:
    print(f"the number:{number}")

print("-----")

for x in range_obj:
    print(f"the element: {x}")

for key in car_obj:
    print(f"the key: {key} => value: {car_obj}.get{key}")

print("-----")

for y in range(1, 20, 5):
    print(f"the y: {y}")

print("==== break/else ====")

for z in range(1, 20, 5):
    print(f"the z: {z}")
    if z > 10:
        print("Reached break")
        break
else:
    print("Looped successfuly")

print("=== while operator ===")
numb = 40
while numb > 0:
    numb -= 10
    print(f"the numb equals {numb}")

print("------")
count = 0
while True:
    count += 1
    x = int(input("Find number "))

    if x == 41:
        print(f"Your food number is {count} steps")
        break
    else:
        print("Wrong, please find again!")
