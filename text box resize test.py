#IMPORTS
from tkinter import *
root = Tk()

#GUI DIMENSIONS
root.geometry("205x200")
root.title("calculator")

#GLOBAL VAR
expression = ""
equation = StringVar()

#FUNCTIONs
def equals_box ():
    global expression
    print(expression)
    expression = equation.get()
    total = str(eval(expression))
    print(total)
    equation.set(total)

def sum_box(number):
    global expression
    try:
        expression = expression + str(number)
        equation.set(expression)
        print(number)
    except:
        equation.set("error")
        expression = ""

def clear ():
    global expression
    expression = ""
    print("clear")
    equation.set(expression)
#text box
number_box = Entry(root, textvariable = equation)
number_box.grid(columnspan = 3,row=0, column=0)

#buttons
one = Button(root, text = "1", command = lambda:sum_box(1)).grid(column = 0, row = 1)
two = Button(root, text = "2", command = lambda:sum_box(2)).grid(column = 1, row = 1)
three = Button(root, text = "3", command = lambda:sum_box(3)).grid(column = 2, row = 1)
four = Button(root, text = "4", command = lambda:sum_box(4)).grid(column = 0, row = 2)
five = Button(root, text = "5", command = lambda:sum_box(5)).grid(column = 1, row = 2)
six = Button(root, text = "6", command = lambda:sum_box(6)).grid(column = 2, row = 2)
seven = Button(root, text = "7", command = lambda:sum_box(7)).grid(column = 0, row = 3)
eight = Button(root, text = "8", command = lambda:sum_box(8)).grid(column = 1, row = 3)
nine = Button(root, text = "9", command = lambda:sum_box(9)).grid(column = 2, row = 3)
zero = Button(root, text = "0", command = lambda:sum_box(0)).grid(column = 0, row = 4)
plus = Button(root, text = "+", command = lambda:sum_box(" + ")).grid(column = 1, row = 4)
minus = Button(root, text = "-", command = lambda:sum_box(" - ")).grid(column = 2, row = 4)
multipy = Button(root, text = "x", command = lambda:sum_box(" * ")).grid(column = 0, row = 5)
divide = Button(root, text = "/", command = lambda:sum_box(" / ")).grid(column = 1, row = 5)
equals = Button(root, text = "=", command = equals_box).grid(column = 2, row = 5)
clear_all = Button(root, text = "AC", command = clear).grid(column = 1, row = 6)
decimal = Button(root, text = ".", command = lambda:sum_box(".")).grid(column = 2, row = 6)









mainloop()