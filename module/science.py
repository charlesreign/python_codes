import module.student as student
# from module.student import Student as student_pk *** this is another way to import packages

stu = student.Student("Charles", 14, "Computer science", ["Algebra"])
print(stu.get_student_courses())
