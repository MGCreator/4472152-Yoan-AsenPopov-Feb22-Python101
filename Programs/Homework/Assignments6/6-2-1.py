class Calculator:
    number1 = 0
    number2 = 0
    number3 = 0

    def __init__(self, num1, num2, num3):
        self.number1 = num1
        self.number2 = num2
        self.number3 = num3

    def sum(self):
        summation = self.number1 + self.number2 + self.number3

        print(f"Result is: {summation}")

    def sub(self):
        subtraction = self.number1 - self.number2 - self.number3

        print(f"Result is: {subtraction}")

    def multi(self):
        multiplication = self.number1 * self.number2 * self.number3

        print(f"Result is: {multiplication}")

    def divide(self):
        division = self.number1 / self.number2 / self.number3

        print(f"Result is: {division}")


while True:

    result = 0
    numbers = []
    isNumber = True
    num = 0

    for item in range(4):
        num = input("A number: ")
        try:
            numbers.append(int(num))
        except:
            break

    sign = num
    equation = Calculator(numbers[0], numbers[1], numbers[2])

    if sign == "+":
        equation.sum()
    elif sign == "-":
        equation.sub()
    elif sign == "*":
        equation.multi()
    elif sign == "/":
        equation.divide()
    else:
        pass
