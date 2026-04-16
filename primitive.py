print("=====number=====")

# in Java and C -  variable is a name of storage location
# in Python - variable is a named of reference

count = 100
print("count:", count)

count_type = type(count)
print(count_type)

# this is what we used to call super string in js
print(f"the count: {count} and the type of variable is{count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("=====string=====")
# METHODS: upper(), lower(), title(), find(), replace()

course = "AI Python Fullstack"
result_1 = type(course)

print(f"the type of course: {result_1}")

result_2 = course.title()
print(f"the result:{result_2}")

result_3 = course.upper()
print(f"the result:{result_3}")

result_4 = course.replace("FullStack", "MasterClass")
print(f"the result: {result_4}")
print(course)

print("=====boolean=====")
# functions > type(), input(), bool(), str()

y = input("Insert your value for y:")
print("y:", y)

result_5 = y.isnumeric()
print(f"Is the input value numeric?: {result_5}")

# TRUTHY vs FALSY value
# TRUTHY: True, 100 , - 100, "abc"
# FALSY: False, 0, "", NONE

test_falsy = "" or False or None or 0
print("The FALSY:", bool(test_falsy))

test_truthy = "MIT"
print("The TRUTHY:", bool(test_truthy))
