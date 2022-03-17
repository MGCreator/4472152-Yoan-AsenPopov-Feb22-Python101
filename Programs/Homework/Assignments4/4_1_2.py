


def sum():

    sum = 0

    for num in numbers:
        sum = num + sum

    return sum


def sub():

    subtraction = numbers[1]


    for num in numbers:
        subtraction = subtraction - num

    return subtraction


def multi():

    multiplication = 1

    for num in numbers:
        multiplication = num * multiplication

    return multiplication


def divide():

    division = numbers[1]
    counter = 1
    for num in numbers:
        if counter == 1:
            division = num / division
            counter += 1

        elif counter < len(numbers):
             print(division)
             print(num)

             division = division / numbers[counter]
             counter += 1
        else:
            break

    return division


while True:

    result = 0
    numbers = []
    isNumber = True
    num1 = 0
    length = 0

    while isNumber == True:
        num1 = input("A number: ")
        try:
            numbers.append(int(num1))
        except:
            break

    length = len(numbers)
    sign = num1

    if sign == "+":
        result = sum()
    elif sign == "-":
        result = sub()
    elif sign == "*":
        result = multi()
    elif sign == "/":
        result = divide()
    else:
        pass
    print(f"Result is: {result}")
