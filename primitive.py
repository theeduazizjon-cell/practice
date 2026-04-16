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
