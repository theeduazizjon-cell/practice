print("=== Iterable Objects ===")
# Iterable objects: string. dictionary, tuple, list, range, map and filter

text = "MIT"

for letter in text:
    print(f"the letter: {letter}")


range_obj = range(3)
print("range_obj", range_obj)

for ele in range_obj:
    print(f"the element:", {ele})


print("=== DICTIONARY ===")
# Dictionary is JSON object!

person = {"name": "Justin", "age": "25", "single": True}
person_obj = dict(name="Justin", age=25, single=True)  # mostly used

print(f"the person: {person}")
print(f"the person: {person_obj}")

name = person_obj["name"]
print("name:", name)

#
# name2 = person_obj["hobby"]
# print("hobby:", name2)

name = person_obj.get("name")
hobby = person.obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name: {name}, hobby {hobby} and balance: {balance}")

del person_obj["single"]
for key in person_obj:
    print(f"the key:{key} => value {person_obj[key]}")
