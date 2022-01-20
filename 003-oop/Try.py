class GamePlay:
    totalSum = 0

    # __init__ this is the constructor of the class

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dom(self, nameOfDom):
        print(f"the name of your dome is {nameOfDom} {self.totalSum}")


player1 = GamePlay()
player1.dom("AKu")
