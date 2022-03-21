original_list = []
manipulated_list = []
command = input("Input a number: ")

while command != '':
    new_command = int(command)
    print(type(new_command))
    original_list.append(new_command)
    manipulated_list.clear()
    for item in original_list:

        if item % 2:
            manipulated_list.append(item)
        else:
            pass
    command = input("Input a number: ")

print(original_list)
print(manipulated_list)