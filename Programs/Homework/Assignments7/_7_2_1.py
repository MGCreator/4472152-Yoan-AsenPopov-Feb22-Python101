import os
import random

os.chdir("d:/Infrastucture")
num = input("Input an int: ")

while True:
    try:
        n = int(num)
        break
    except ValueError:
        num = input("Input an int: ")

with open('random.txt', 'w') as f:
    list_nums = []
    for i in range(n):
        list_nums.append(str(random.randint(0, 100)))

    strings = ''
    for x in range(len(list_nums)):
        strings = strings + list_nums[x]
        if x + 1 != len(list_nums):
            strings = strings + ' '
        else:
            pass

    print(strings)
    f.write(strings)
