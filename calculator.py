# Calculator using tkinter by Aiden C
# Built for Comp Sci on 11/28/22

# Import modules
import tkinter
from tkinter import *
import math

# Create Window
master = Tk()
master.geometry("400x600")
master.title("Aiden's Calculator")

# Define Container And Modifier Objects
#   - Pixler helps restrict button sizes to pixel measurements for exact sizing
pixeler = tkinter.PhotoImage(width=1, height=1)

#   - Scrollbar controls vertical scrolling for the input box
scrollbar = Scrollbar(master, orient='horizontal')
scrollbar.pack(side=BOTTOM, fill=X)

#   - Textboxframe handles sizing for the input box because input boxes don't handle sizing well themselves
textboxframe = Frame(master)
textboxframe.columnconfigure(0, weight=10)
textboxframe.grid_propagate(False)

#   - Defining the input box and applying the scrollbar to it
textbox = Text(textboxframe, xscrollcommand=scrollbar.set, padx=10, wrap="none", state="disabled")
textbox.grid(sticky="we")
scrollbar.config(command=textbox.xview)

#   - Defining variables
boxvar = ""
backspace = True


# Handle Button Presses & Key-presses
def updatebox(action):
    global boxvar
    global backspace
    backspace = True
    boxvar = str(boxvar) + str(action)
    # Note: I have to set the state to normal in order to edit inputbox contents, but I have to change it back to disabled to keep the user from directly typing into the box
    textbox.config(state="normal")
    textbox.delete(0.0, "end")
    textbox.insert(0.0, boxvar)
    textbox.config(state="disabled")


# Handle The AC Button and Backspace
def clearbox(modifier):
    global boxvar
    global backspace
    textbox.config(state="normal")
    if backspace:
        boxvar = str(boxvar)[:-1]
        textbox.delete(0.0, "end")
        textbox.insert(0.0, boxvar)
    else:
        boxvar = ""
        textbox.delete(0.0, "end")
    if modifier == 1:
        backspace = False
    textbox.config(state="disabled")


# Handle Evaluating Equation Results
def evaluatebox():
    global boxvar
    global backspace
    backspace = True
    textbox.config(state="normal")
    textbox.delete(0.0, "end")
    try:
        if boxvar != "":
            boxvar = eval(str(boxvar))
            if int(boxvar) >= 1:
                # Adjusting format to avoid displaying scientific notation
                boxvar = str(format(boxvar, '.0f'))
            textbox.insert(0.0, boxvar)
            print("Calculator Output: " + str(boxvar))
            backspace = False
        else:
            boxvar = 0
            textbox.insert(0.0, boxvar)

    # Error Handling
    except OverflowError:
        textbox.insert(0.0, "Err: Overflow")
        print("Error: Output value larger then str length limit")
    except ZeroDivisionError:
        textbox.insert(0.0, "Err: Div/0")
        print("Error: Bruv, you can't divide by 0")
    except SyntaxError:
        textbox.insert(0.0, "Err: Syntax")
        print("Error: Something is wrong with your input equation. Common causes are equation starting with operator or 0, no equation inputted...")
    except TypeError:
        print("sus")
    textbox.config(state="disabled")


# Create Button Objects
one = Button(master, text="1", command=lambda: updatebox(1))
two = Button(master, text="2", command=lambda: updatebox(2))
three = Button(master, text="3", command=lambda: updatebox(3))
AC = Button(master, text="AC", command=lambda: clearbox(1))
four = Button(master, text="4", command=lambda: updatebox(4))
five = Button(master, text="5", command=lambda: updatebox(5))
six = Button(master, text="6", command=lambda: updatebox(6))
divide = Button(master, text="÷", command=lambda: updatebox("/"))
seven = Button(master, text="7", command=lambda: updatebox(7))
eight = Button(master, text="8", command=lambda: updatebox(8))
nine = Button(master, text="9", command=lambda: updatebox(9))
multiply = Button(master, text="x", command=lambda: updatebox("*"))
point = Button(master, text=".", command=lambda: updatebox("."))
zero = Button(master, text="0", command=lambda: updatebox(0))
subtract = Button(master, text="-", command=lambda: updatebox("-"))
add = Button(master, text="+", command=lambda: updatebox("+"))
equals = Button(master, text="=", command=lambda: evaluatebox())

# Define Button Object Names In An Array For Easy Handling
buttonnames = ["null", one, two, three, AC, four, five, six, divide, seven, eight, nine, multiply, point, zero, subtract, add, equals]


# Auto-Resize Handler
def resize():
    # Top Text Box Resize Handler
    textboxframe.config(width=round(master.winfo_width()), height=round(master.winfo_height() / 3.5))
    textboxframe.place(y=0, x=0)
    textbox.config(pady=(round((master.winfo_height() / 7) - (master.winfo_height() / 12))), font=("Arial", (int(master.winfo_height() / 10))))

    # Button Resizing Handler
    global buttonnames
    for i in range(1, 18):
        buttonnames[i].place(x=((master.winfo_width() / 4) * ((i - ((math.ceil(i / 4) - 1) * 4)) - 1)), y=((master.winfo_height() / 7) * ((math.ceil(i / 4) - 1) + 2)), anchor=NW)
        buttonnames[i].config(width=round(master.winfo_width() / 4), height=round(master.winfo_height() / 7), compound="center", image=pixeler, padx=0, pady=0, font="Arial %s" % (int(master.winfo_height() / 20)))
        equals.config(width=master.winfo_width())


# Binding Key-presses To Functions
master.bind('1', lambda event: updatebox(1))
master.bind('2', lambda event: updatebox(2))
master.bind('3', lambda event: updatebox(3))
master.bind('4', lambda event: updatebox(4))
master.bind('5', lambda event: updatebox(5))
master.bind('6', lambda event: updatebox(6))
master.bind('7', lambda event: updatebox(7))
master.bind('8', lambda event: updatebox(8))
master.bind('9', lambda event: updatebox(9))
master.bind('0', lambda event: updatebox(0))
master.bind('+', lambda event: updatebox("+"))
master.bind('=', lambda event: updatebox("+"))
master.bind('-', lambda event: updatebox("-"))
master.bind('_', lambda event: updatebox("-"))
master.bind('/', lambda event: updatebox("/"))
master.bind('*', lambda event: updatebox("*"))
master.bind('x', lambda event: updatebox("*"))
master.bind('.', lambda event: updatebox("."))
master.bind('^', lambda event: updatebox("**"))
master.bind('(', lambda event: updatebox("("))
master.bind(')', lambda event: updatebox(")"))
master.bind('%', lambda event: updatebox("%"))
master.bind('<Return>', lambda event: evaluatebox())
master.bind('<BackSpace>', lambda event: clearbox(2))

# Binding Resize To Resize Function
master.bind("<Configure>", lambda event: resize())

# Close Out Main Loop
mainloop()
