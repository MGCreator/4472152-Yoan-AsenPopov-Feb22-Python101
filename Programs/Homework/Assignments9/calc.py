class Calculator:
    number1 = 0
    number2 = 0
    number3 = 0



    def __init__(self, nums):
        self.nums = nums
        

    def sum(self):
        summation = 0
        for i in self.nums:
            summation += i

        return summation

    def sub(self):
        subtraction = self.nums[0]
        self.nums.pop(0)
        for i in self.nums:
            subtraction -= i

        return subtraction

    def multi(self):
        multiplication = self.nums[0]
        self.nums.pop(0)
        for i in self.nums:
            multiplication *= i

        return multiplication

    def divide(self):
        division = self.nums[0]
        self.nums.pop(0)
        for i in self.nums:
            division /= i

        return division

if __name__ == "__main__":

    while True:

        result = 0
        numbers = []
        num = 0

        while True:
            num = input("A number: ")
            try:
                numbers.append(int(num))
            except:
                break
        
        sign = num
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
