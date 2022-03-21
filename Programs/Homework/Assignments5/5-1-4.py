list_of_num = [1, 2, 2, 2, 3, 1, 4, 2, 3, 6, 7, 9, 7, 3]
new_list_of_num = []
for item in list_of_num:
    if item not in new_list_of_num:
        new_list_of_num.append(item)

print(new_list_of_num)
