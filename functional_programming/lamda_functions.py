# lambda expressions work well with functional programming
# lambda expressions are anonymous functions that are called once and exits
from functools import reduce

# my_list = [2, 4, 6, 7, 3, 1, 9]
#
# print(list(map(lambda item: item * 2, my_list)))
#
# print(list(filter(lambda item: item % 2 == 0, my_list)))
#
# print(reduce(lambda item, item2: item + item2, my_list))

# exercise............................
my_list = [5, 4, 3]

# squaring the items in the list
print(list(map(lambda item: item ** 2, my_list)))

# sorting list using lambda expression
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])

print(sorted(a, key=lambda x: x[1]))

print(a)
