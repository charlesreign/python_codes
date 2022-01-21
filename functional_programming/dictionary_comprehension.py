simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

my_dict = {key: value * 2 for key, value in simple_dict.items()}

print(my_dict)

my_dict2 = {val: val * 2 for val in [1, 2, 3, 4, 5, 6, 7]}

print(my_dict2)
