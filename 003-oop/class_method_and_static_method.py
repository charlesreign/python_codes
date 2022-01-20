class GamePlay:
    totalSum = 0

    # __init__ this is the constructor of the class

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dom(self, nameOfDom):
        print(f"the name of your dome is {nameOfDom} {self.totalSum}")

    @classmethod
    def adding_something(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_something_2(num1, num2):
        return num1 + num2


print(GamePlay.adding_something(20, 30))

print(GamePlay.adding_something_2(87, 34))
