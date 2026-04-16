'''
Functions 
1 - Define and Call 
2 - Parametr and Argument 
3 - Keyword and default arguments 
4 - Scope
'''
print("=== Define and Call ===")
# build in function > print() , type(), input() and etc
# Functions - reusable block of code , malum bir mantiqni ishga churib beradigan code block
# Instead of block {} in Java , we use indentation in Python

# example_1

# Define - build


def greet(a):
    print(f"How do you do?, {a}")


def greeting(b):
    print("Greeting is executed ")
    return f"Hi {b}"


# Call - excecute
result_1 = greet("Alex")
print("result1:", result_1)

result_2 = greeting("Justin")
print("result2:", result_2)
