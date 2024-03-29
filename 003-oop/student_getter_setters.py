class Student():
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


student_one = Student("Charlie", 12, "Computer Science",
                      ["Programming I", "Programming II", "Discrete Structures & Theory",
                       "Programming III", "Data Structures & Algorithms",
                       "Computer Organization & Architecture", "Software Engineering", "Operating Systems"])

student_one.set_student_age(19)
print(student_one.get_student_age())


class Science(Student):
    def __init__(self, name, age, programme, courses):
        super().__init__(name, age, programme, courses)


sci = Science("Charlie", 12, "Science", ["Programming I"])
print(sci.get_student_programme())
