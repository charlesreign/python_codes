# age = input("What is your age?: ")
#
# if int(age) < 18:
#     print("Sorry, you are too young to drive this car. Powering off")
# elif int(age) > 18:
#     print("Powering On. Enjoy the ride!");
# elif int(age) == 18:
#     print("Congratulations on your first year of driving. Enjoy the ride!")

# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get
# prompted for age. Notice the benefit in having checkDriverAge() instead of copying and pasting the function
# every time?

# def checkDriverAge():
#     age = input("What is your age?: ")
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
#
#
# checkDriverAge()


# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you
# enter: checkDriverAge(92); it returns "Powering On. Enjoy the ride!" also make it so that the default age is set to
# 0 if no argument is given.

# def checkDriverAge2(age=0):
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
#
#
# checkDriverAge2(18)


# return the highest even number from the list

listOfHighestItem = []


def highest_even(li):
    for items in li:
        if items % 2 == 0:
            listOfHighestItem.append(items)
    return max(listOfHighestItem)
    # or
    # listOfHighestItem.sort()
    # return listOfHighestItem[-1]


print(highest_even([1, 20, 34, 56, 34, 2, 3, 45]))
