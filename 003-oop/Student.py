class Student:
    __schoolName = 'XYZ School'  # private class attribute

    def __init__(self, name, age):
        self._name = name  # private instance attribute
        self.__salary = age  # private instance attribute

    def __display(self):  # private method
        print('This is private method.')


std = Student("Bill", 25)
print(std.__name)
