
num = float(input("Number: "))
command = num

sum = 0
avg_value = 0
min_value = 0
max_value = 0

numbers_list = []
while command != 0:
    numbers_list.append(num)
    num = float(input("Number: "))
    command = num
print(numbers_list)
list_count = len(numbers_list)
print(list_count)
for element in numbers_list:
    sum += element
avg_value = sum / list_count
min_value = min(numbers_list)
max_value = max(numbers_list)


int(avg_value)
int(min_value)
int(max_value)

print(f"Sum is {sum}. Average is {avg_value}. \nMinimum is {min_value}. Maximum is {max_value}")


