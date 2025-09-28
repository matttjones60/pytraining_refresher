class Robot_Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def bark(self):
        return "Woof!"

    def sit(self):
        return f"{self.name} is now sitting."

    def roll_over(self):
        return f"{self.name} rolled over!"
    
my_dog = Robot_Dog("Rex", "blue", 5)

print(my_dog.name)
print(my_dog.color)

my_dog.sit()