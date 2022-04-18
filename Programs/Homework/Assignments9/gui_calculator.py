from tkinter import *
import calc

root = Tk()
root.title("Calculator")

numbers = []
global sign
sign = ""

display = Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=10,pady=10)
#display.insert(0, "0")

def display_num(num):
    
    current_num = display.get()
    display.delete(0, END)
    display.insert(0, current_num + str(num))


def clear():
    display.delete(0, END)
    numbers.clear()


def add():
    global sign
    sign = "+"
    previous_num = display.get()
    global number
    number = int(previous_num)
    numbers.append(number)
    display.delete(0, END)


def subtract():
    global sign
    sign = "-"
    previous_num = display.get()
    global number
    number = int(previous_num)
    numbers.append(number)
    display.delete(0, END)


def multiplication():
    global sign
    sign = "*"
    previous_num = display.get()
    global number
    number = int(previous_num)
    numbers.append(number)
    display.delete(0, END)


def divide():
    global sign
    sign = "/"
    previous_num = display.get()
    global number
    number = int(previous_num)
    numbers.append(number)
    display.delete(0, END)
    

def equal():
    second_num = int(display.get())
    numbers.append(second_num)
    display.delete(0, END)
    equation = calc.Calculator(numbers)
    result = 0
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
    display.insert(0, result)


buttn1 = Button(root, text="1",padx=40, pady=20, command=lambda: display_num(1))
buttn2 = Button(root, text="2",padx=40, pady=20, command=lambda: display_num(2))
buttn3 = Button(root, text="3",padx=40, pady=20, command=lambda: display_num(3))
buttn4 = Button(root, text="4",padx=40, pady=20, command=lambda: display_num(4))
buttn5 = Button(root, text="5",padx=40, pady=20, command=lambda: display_num(5))
buttn6 = Button(root, text="6",padx=40, pady=20, command=lambda: display_num(6))
buttn7 = Button(root, text="7",padx=40, pady=20, command=lambda: display_num(7))
buttn8 = Button(root, text="8",padx=40, pady=20, command=lambda: display_num(8))
buttn9 = Button(root, text="9",padx=40, pady=20, command=lambda: display_num(9))
buttn0 = Button(root, text="0",padx=40, pady=20, command=lambda: display_num(0))
buttn_clear = Button(root, text="clear",padx=78, pady=20, command=clear)
buttn_add = Button(root, text="+",padx=39, pady=20, command=add)
buttn_equal = Button(root, text="=",padx=87, pady=20, command=equal)
buttn_sub = Button(root, text="-",padx=40, pady=20, command=subtract)
buttn_times = Button(root, text="*",padx=40, pady=20, command=multiplication)
buttn_divide = Button(root, text="/",padx=40, pady=20, command=divide)

buttn1.grid(row=3, column=0)
buttn2.grid(row=3, column=1)
buttn3.grid(row=3, column=2)
buttn4.grid(row=2, column=0)
buttn5.grid(row=2, column=1)
buttn6.grid(row=2, column=2)
buttn7.grid(row=1, column=0)
buttn8.grid(row=1, column=1)
buttn9.grid(row=1, column=2)
buttn0.grid(row=4, column=0)
buttn_clear.grid(row=4, column=1, columnspan=2)
buttn_add.grid(row=5, column=0)
buttn_equal.grid(row=5, column=1, columnspan=2)
buttn_sub.grid(row=6, column=0)
buttn_times.grid(row=6, column=1)
buttn_divide.grid(row=6, column=2)





root.mainloop()