# Dunder - double underlines:  __builtins__ , __init__

# example_1
message = "Everything in pyhton is an object"
print(message)

result = type(message)
print("result:", result)


''' This is multiple line comments 
In Pyhton , there are builtin tools:
1 - TYPES > int float str list dict 
2 - FUNCTION > print() , len(), input(), type()
3 - CONSTANTS > True or False None 
'''
print(dir(__builtins__))
