"""
Encapsulation 
1 - Encapsulation 
2 - Inheritance 
3 - Polimorpism 
"""

print("=== Inheritance ===")

# Parent -> Child
# Parent provides only public & protected properties(state + method) to children![]


class Animal():  # parent
    # even if you are not going to use the brakets , python will use them by default
    # state
    description = "This class is parent for animal"

    # constructor
    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child , extended. Parent can pass it's property
    # state

    # constructor
    def __init__(self, name, sound,  voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you")

    def make_voice(self):
        print(f"the {self.name} says {self.sound}")


class cat(Animal):  # Child , extended. Parent can pass it's property
    # state

    # constructor
    def __init__(self, name, sound,  voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child , extended. Parent can pass it's property
    # state

    # constructor
    def __init__(self, name, sound,  voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim")


dog = Dog("Rex", "wow", True)
cat = cat("Tom", "myeow", True)
fish = Fish("Nemo", "zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("---")
dog.make_voice()
fish.make_voice()

print("---")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("dog.status:", dog.status)
print("cat.status:", cat.status)


print("=== Polimorphism ===")
dog.make_voice()
fish.make_voice()

print("---")
# fish -> Fish -> Animal -> Object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print("result:", result)

data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)
