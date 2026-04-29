"""
Package and Debugging
1) Python Packages & Core Package
2) Package manager & external package
3) Debugging
"""
"""

from PIL import Image
import turtle
print("=== Python pakcages & Core packages ===")
# Python Packages/Modules: Core, File and External

# Core pakcages > https://docs.python.org/3/library

# Core packages
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
t.circle(100)

turtle.done()

my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content: ", content)
finally:
    my_file.close()

# with
with open("material/message.txt", "r") as your_files:
    your_content = your_file.read()
    print("your_content: ", your_content)


print("DONE")

print("=== Package manager & External Package ===")

# Package manager: PIP
# External packages: https://pypi.org/

with Image.open("material/pngwing.com.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")

"""
print("=== Debugging ===")


def get_summary(*args):  # Define
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount


test = 100
result = get_summary(1, 2, 3, 4, 5)  # Call
print("result: ", result)
