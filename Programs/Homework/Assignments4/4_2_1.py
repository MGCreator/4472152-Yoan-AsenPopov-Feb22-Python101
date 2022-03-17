def triangle (row):
    numberOfStars = 1
    numberOfSpace = row - 1

    for i in range(row):
        count = 0
        count1 = 0
        while count < numberOfSpace:
            print(" ", end='')
            count += 1
        while count1 < numberOfStars:
            print("*", end='')
            count1 += 1
        print("")
        numberOfSpace -= 1
        numberOfStars += 1

print(triangle(int((input("Number: ")))))

