# for items in 'Hello world':
#     print(items)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# total_sum = 0
#
# for elements in my_list:
#     total_sum += elements
#
# print(total_sum)
#
# for items in range(1, 20, 2):
#     print(items)


# Exercise! Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be
# '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
#
# for items in picture:
#     for element in items:
#         if element == 0:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print('')


# find the duplicates
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# dup = []
#
# for elements in some_list:
#     if some_list.count(elements) > 1:
#         if elements not in dup:
#             dup.append(elements)
# print(dup)


x = [10]
y = [10]

print(x is y)