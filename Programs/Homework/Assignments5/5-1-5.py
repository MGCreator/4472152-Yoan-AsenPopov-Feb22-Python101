command = int(input("Input a number: "))
list_of_nums = []
while command != '':
    for num in range(command + 1):
        squared_num = num**2
        list_of_nums.append(squared_num)
    print(list_of_nums)
    command = int(input("Input a number: "))