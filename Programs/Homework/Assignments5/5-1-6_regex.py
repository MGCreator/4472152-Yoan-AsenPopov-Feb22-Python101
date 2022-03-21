import re
original_list = []
manipulated_list = []
command = input("Input a number: ")
nums = [int(nums) for nums in re.findall('\d+', command)]
#(r'-?\d+\.?\d*', command)
print(type(nums))

original_list = nums


for item in original_list:

    if item % 2:
        manipulated_list.append(item)
    else:
        pass

print(original_list)
print(manipulated_list)