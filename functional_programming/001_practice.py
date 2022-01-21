from functools import reduce


def multiply_items(items):
    return items * 2


def get_only_even_numbers(items):
    return items % 2 != 0


def accumulator(acc, item):
    return acc + item


my_list = [2, 4, 6, 7, 3, 1, 9]
another_list = [20, 12, 13, 45, 67, 78]

# using map
print(list(map(multiply_items, my_list)))

# using filter
print(list(filter(get_only_even_numbers, my_list)))

# using zip
print(list(zip(my_list, another_list)))

# using reduce
print(reduce(accumulator, another_list, 0))
