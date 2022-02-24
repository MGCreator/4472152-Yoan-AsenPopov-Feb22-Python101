
num = (input("Number: "))
command = num
while command != 'q':

    if int(num) > 0:
      print("Number is positive.")
    elif int(num) < 0:
        print("Number is negative")
    elif int(num) == 0:
       print("Number is zero")
    num = input("Number: ")
    command = num