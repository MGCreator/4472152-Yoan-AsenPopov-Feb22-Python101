list_of_names = []
command = input("Input a name: ")
while command != '':

    list_of_names.append(command)
    command = input("Input a name: ")

print(list_of_names)
print(sorted(list_of_names, reverse=True))
