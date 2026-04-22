"""
Oparators and Conditions 
1 - opeartors 
2 - conditions 
3 - logical operators 
"""

print("==== Operators ====")
# + - > >= < <= * / // %% += **

a = 19
b = 5
print("a>b", a > b)
print("a/b", a/b)
print("a*b", a*b)

result = a // b
left = a % b
print(f"the result: {result} and the reaminder:{left}")

# a = a + 100
a += 100
print("a:", a)

print("it is b squared", b**2)

print("="*5)  # its okay in python

c = dict(name="Martin", age=35)
d = dict(name="Martin", age=35)
e = c

print("c==d", c == d)  # only value
print(id(c), id(d))

data = c is d
print("c is d", data)

print("=== Conditions ===")
x = 5

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")


print("=== Logical Operators ===")

age = 18
person = None

if age > 16:
    person = "adult"
else:
    person = "child"

print("person", person)

# Ternary Operator

age = 20
person = "adult" if age > 18 else "minor"
print("person:", person)

print("-----")

is_student = True
is_admin = False
is_guest = True
is_parent = True

if not is_student:  # not operator
    print("executed")
elif is_admin:
    print("Please go to this office")
elif is_guest or is_parent:
    print("Waiting room is over there")
else:
    print("Other cases")
