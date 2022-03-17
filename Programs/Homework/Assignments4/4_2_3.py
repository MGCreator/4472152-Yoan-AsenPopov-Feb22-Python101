
def isPrime(num):
    Prime = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                Prime = False
                break
    if Prime:
        print(num)
    else:
        pass


def printPrime(num):
    for i in range(2, num + 1):
        isPrime(i)


num = int(input("Number: "))
printPrime(num)
