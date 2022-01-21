my_list2 = {items for items in 'hello'}

my_list3 = {items for items in range(0, 101)}

my_list4 = {items * 3 for items in range(0, 20)}

my_list5 = {items * 3 for items in range(0, 40) if items % 2 == 0}
print(my_list5)
