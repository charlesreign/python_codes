class Student:
    __student_name = None
    __student_age = None
    __student_programme = None
    __student_courses = []

    def __init__(self, name, age, programme, courses):
        self.__student_name = name
        self.__student_age = age
        self.__student_programme = programme
        self.__student_courses = courses

    # ........................getters..............
    def get_student_name(self):
        return self.__student_name

    def get_student_age(self):
        return self.__student_age

    def get_student_programme(self):
        return self.__student_programme

    def get_student_courses(self):
        return self.__student_courses

    # ........................setters..............
    def set_student_name(self, name):
        self.__student_name = name

    def set_student_age(self, age):
        self.__student_age = age

    def set_student_programme(self, programme):
        self.__student_programme = programme

    def set_student_courses(self, courses):
        self.__student_programme = courses
