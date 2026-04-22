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
