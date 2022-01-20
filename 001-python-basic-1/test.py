# print(bin('A'))
# print(int('0b101', 2))

# iq = 190
# print(bin(iq))
#
# print(int('0b10111110',2))

# long_text = '''
# Triple single
# Quote is used for multi line text
# this is good to know
# '''
#
# print(long_text)
#
# print(type(5))
#
# print("it's me" + 'it\'s you')

# name = "Charles"
# age = 20
#
# # this is how string formatting is done in python 3
# print(f"hello {name} you are {age} years old")
#
# # this is how string formatting is done in python 2
# print("hello {new_name} you are {new_age} years old".format(new_name='charlie', new_age=18))
#
# print(len(name))

name = "Charles Reign Gold"

"""print(name[0:len(name):1])
print(name[2:5:1])

print(name.count('Reign'))"""

# name = "Charles"
# print(name[0])

# ...........................Working with list

"""amazon_cart = [
    'note books',
    'bible',
    'sunglasses',
    'toys'
]

amazon_cart[0] = 'laptop'

new_cart = amazon_cart

new_cart[0] = 'gun'

print(amazon_cart)

new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)

# access "Oranges" and print it:
basket = ["Banana",
          ["Apples", ["Oranges"], "Blueberries"]]

print(basket[1][1][0])

# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.pop(0)
basket.remove("Banana")

# 2. Remove "Blueberries" from the list.
basket.pop()

# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwi')

# 4. Add "Apples" at the beginning of the list
basket.insert(0, "Apples")

# 5. Count how many apples in the basket
basket.count("Apples")

# 6. empty the basket
basket.clear()

print(basket)"""

# print(list(range(1,10)))

# list unpacking the assigning a variable to elements in a list
name, age, dob = ["charles", 20, 2002]
print(name)
print(age)
print(dob)
