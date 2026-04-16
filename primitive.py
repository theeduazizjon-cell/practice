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
