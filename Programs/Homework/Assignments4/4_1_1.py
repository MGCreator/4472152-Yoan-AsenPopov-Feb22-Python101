result = 0


def sum(a, b):
    sum = a + b
    return sum


def sub(a, b):
    subtraction = a - b
    return subtraction


def multi(a, b):
    multiplication = a * b
    return multiplication


def divide(a, b):
    division = a / b
    return division


while True:
    num1 = int(input("A number: "))
    num2 = int(input("Second number: "))
    sign = input("Input a sign: ")
    if sign == "+":
        result = sum(num1, num2)
    elif sign == "-":
        result = sub(num1, num2)
    elif sign == "*":
        result = multi(num1, num2)
    elif sign == "/":
        result = divide(num1, num2)
    else:
        pass
    print(f"Result is: {result}")
