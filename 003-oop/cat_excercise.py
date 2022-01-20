# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("pussy1", 12)
cat2 = Cat("pussy2", 15)
cat3 = Cat("pussy3", 78)


# 2 Create a function that finds the oldest cat
def getOldestCat(listOfCatAge):
    catAges = []
    for items in listOfCatAge:
        catAges.append(items)
    print(f"The oldest cat is {max(catAges)} years old.")


getOldestCat([cat1.age, cat2.age, cat3.age])

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
