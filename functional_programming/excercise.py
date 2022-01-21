from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def make_all_items_capitalize(items):
    capitalized_pets = []
    for ele in items:
        capitalized_pets.append(ele.upper())
    return capitalized_pets


print(make_all_items_capitalize(my_pets))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1, 2]

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def new_filter_score(list_scores):
    return list_scores > 50


print(list(filter(new_filter_score, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))

# def filter_score(list_scores):
#     new_scores = []
#     for items in list_scores:
#         if items > 50:
#             new_scores.append(items)
#     return new_scores


pp = list(zip(my_numbers, scores))

# print(my_numbers, end='')
# print(scores, end='')

# print(pp)
#
# total_element = 0
# for ele1, ele2 in pp:
#     sum_ele = ele1 + ele2
#     total_element = total_element + sum_ele
#
# print(total_element)