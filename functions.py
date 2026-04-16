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


def greet(a):  # void
    print(f"How do you do?, {a}")  # a is a parametr


def greeting(b):  # returning function
    print("Greeting is executed ")
    return f"Hi {b}"


# Call - excecute
result_1 = greet("Alex")  # argument
print("result1:", result_1)

result_2 = greeting("Justin")  # argument
print("result2:", result_2)

print("===== Keyword & Defualt arguments =====")
# Define


def give_greet(name, age=21):
    print("give greet is excecuted")
    return f"Hi {name}, you are {age} years old!"

# Call


# name and age are called keywords argument to make our code more clean and readable
result_3 = give_greet(name="Alex", age=21)
print("result_3:", result_3)

result_4 = give_greet("Alex")
print("result_4:", result_4)
