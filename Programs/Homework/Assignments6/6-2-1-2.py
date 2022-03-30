class Calculator:

    def __init__(self, num):

        self.num = num

    def sum(self):
        summation = 0
        for item in self.num:
            summation = item + summation

        return summation

    def sub(self):

        subtraction = numbers[1]

        for item in self.num:
            subtraction = subtraction - item

        return subtraction

    def multi(self):

        multiplication = 1

        for item in self.num:
            multiplication = item * multiplication

        return multiplication

    def divide(self):

        division = self.num[1]
        counter = 1
        for item in self.num:
            if counter == 1:
                division = item / division
                counter += 1

            elif counter < len(numbers):
                print(division)
                print(item)

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

    while isNumber:
        num1 = input("A number: ")
        try:
            numbers.append(int(num1))
        except:
            break

    length = len(numbers)
    sign = num1
    equation = Calculator(numbers)

    if sign == "+":
        result = equation.sum()
    elif sign == "-":
        result = equation.sub()
    elif sign == "*":
        result = equation.multi()
    elif sign == "/":
        result = equation.divide()
    else:
        pass
    print(f"Result is: {result}")
