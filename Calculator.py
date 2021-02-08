from tkinter import *
import operator

def calculate(x, y, operator, get_operator = {
                '+' : operator.add,
                '-' : operator.sub,
                '*' : operator.mul,
                '/' : operator.__truediv__,
                '%' : operator.mod,
                '^' : operator.xor,
                }.get):
    x, y = int(x), int(y)
    return get_operator(operator)(x, y)

def click_one():
    global x
    global y
    global first_value
    global second_value
    if (first_value):
        x *= 10
        x += 1
        lbl.configure(text=x, font=("Arial Bold", 20))
    if (second_value):
        y *= 10
        y += 1
        lbl.configure(text=y, font=("Arial Bold", 20))

def click_two():
    global x
    global y
    global first_value
    global second_value
    if (first_value):
        x *= 10
        x += 2
        lbl.configure(text=x, font=("Arial Bold", 20))
    if (second_value):
        y *= 10
        y += 2
        lbl.configure(text=y, font=("Arial Bold", 20))

def click_three():
    global x
    global y
    global first_value
    global second_value
    if (first_value):
        x *= 10
        x += 3
        lbl.configure(text=x, font=("Arial Bold", 20))
    if (second_value):
        y *= 10
        y += 3
        lbl.configure(text=y, font=("Arial Bold", 20))

def click_four():
    global x
    global y
    global first_value
    global second_value
    if (first_value):
        x *= 10
        x += 4
        lbl.configure(text=x, font=("Arial Bold", 20))
    if (second_value):
        y *= 10
        y += 4
        lbl.configure(text=y, font=("Arial Bold", 20))

def click_five():
    global x
    global y
    global first_value
    global second_value
    if (first_value):
        x *= 10
        x += 5
        lbl.configure(text=x, font=("Arial Bold", 20))
    if (second_value):
        y *= 10
        y += 5
        lbl.configure(text=y, font=("Arial Bold", 20))

def click_six():
    global x
    global y
    global first_value
    global second_value
    if (first_value):
        x *= 10
        x += 6
        lbl.configure(text=x, font=("Arial Bold", 20))
    if (second_value):
        y *= 10
        y += 6
        lbl.configure(text=y, font=("Arial Bold", 20))

def click_seven():
    global x
    global y
    global first_value
    global second_value
    if (first_value):
        x *= 10
        x += 7
        lbl.configure(text=x, font=("Arial Bold", 20))
    if (second_value):
        y *= 10
        y += 7
        lbl.configure(text=y, font=("Arial Bold", 20))

def click_eight():
    global x
    global y
    global first_value
    global second_value
    if (first_value):
        x *= 10
        x += 8
        lbl.configure(text=x, font=("Arial Bold", 20))
    if (second_value):
        y *= 10
        y += 8
        lbl.configure(text=y, font=("Arial Bold", 20))

def click_nine():
    global x
    global y
    global first_value
    global second_value
    if (first_value):
        x *= 10
        x += 9
        lbl.configure(text=x, font=("Arial Bold", 20))
    if (second_value):
        y *= 10
        y += 9
        lbl.configure(text=y, font=("Arial Bold", 20))

def click_zero():
    global x
    global y
    global first_value
    global second_value
    if (first_value):
        x *= 10
        lbl.configure(text=x, font=("Arial Bold", 20))
    if (second_value):
        y *= 10
        lbl.configure(text=y, font=("Arial Bold", 20))

def click_plus():
    global operator
    global first_value
    global second_value
    first_value = False
    second_value = True
    operator = '+'


def click_min():
    global operator
    global first_value
    global second_value
    first_value = False
    second_value = True
    operator = '-'

def click_mul():
    global operator
    global first_value
    global second_value
    first_value = False
    second_value = True
    operator = '*'

def click_div():
    global operator
    global first_value
    global second_value
    first_value = False
    second_value = True
    operator = '/'

def click_equ():
    global operator
    global x
    global y
    if(operator == '+'):
        x += y
    if(operator == '-'):
        x -= y
    if(operator == '*'):
        x *= y
    if(operator == '/'):
        x /= y
    lbl.configure(text=x, font=("Arial Bold", 20))

def click_reset():
    global x
    global y
    global first_value
    global second_value
    x = 0
    y = 0
    first_value = True
    second_value = False
    lbl.configure(text = '')

master = Tk()
master.title("Calculator")
master.geometry('350x300')
lbl = Label(master, width = 10)
lbl.grid(column=2, row = 0)
first_value = True
second_value = False
x = 0
y = 0
plus_button = Button(master, width = 2, text = '+', font=("Arial Bold", 20), bg = '#A877BA', command=click_plus)
plus_button.grid(column = 0, row = 3)
minus_button = Button(master, width = 2, text = '-', font=("Arial Bold", 20), bg = '#A877BA', command=click_min)
minus_button.grid(column = 0, row = 4)
mult_button = Button(master, width = 2, text = '*', font=("Arial Bold", 20), bg = '#A877BA', command=click_mul)
mult_button.grid(column = 0, row = 5)
div_button = Button(master, width = 2, text = '/', font=("Arial Bold", 20), bg = '#A877BA', command=click_div)
div_button.grid(column = 0, row = 6)
equ_button = Button(master, width = 3, text = '=', font=("Arial Bold", 20), bg = '#A877BA', command=click_equ)
equ_button.grid(column = 1, row = 6)
reset = Button(master, width = 4, text = 'Reset', font=("Arial Bold", 10), bg = '#A877BA', command=click_reset)
reset.grid(column = 3, row = 6, sticky="nsew")
number_one = Button(master, width = 3, text = 1, font=("Arial Bold", 20), bg = '#A877BA', command=click_one)
number_one.grid(column = 1, row = 3)
number_two = Button(master, width = 2, text = 2, font=("Arial Bold", 20), bg = '#A877BA', command=click_two)
number_two.grid(column = 2, row = 3, sticky="nsew")
number_three = Button(master, width = 3, text = 3, font=("Arial Bold", 20), bg = '#A877BA', command=click_three)
number_three.grid(column = 3, row = 3)
number_four = Button(master, width = 3, text = 4, font=("Arial Bold", 20), bg = '#A877BA', command=click_four)
number_four.grid(column = 1, row = 4)
number_five = Button(master, width = 2, text = 5, font=("Arial Bold", 20), bg = '#A877BA', command=click_five)
number_five.grid(column = 2, row = 4, sticky="nsew")
number_six = Button(master, width = 3, text = 6, font=("Arial Bold", 20), bg = '#A877BA', command=click_six)
number_six.grid(column = 3, row = 4)
number_seven = Button(master, width = 3, text = 7, font=("Arial Bold", 20), bg = '#A877BA', command=click_seven)
number_seven.grid(column = 1, row = 5)
number_eight = Button(master, width = 2, text = 8, font=("Arial Bold", 20), bg = '#A877BA', command=click_eight)
number_eight.grid(column = 2, row = 5, sticky="nsew")
number_nine = Button(master, width = 3, text = 9, font=("Arial Bold", 20), bg = '#A877BA', command=click_nine)
number_nine.grid(column = 3, row = 5)
number_zero = Button(master, width = 2, text = 0, font = ("Arial Bold", 20), bg = '#A877BA', command=click_zero)
number_zero.grid(column = 2, row = 6, sticky="nsew")
master.mainloop()
#x = input()
#print("Will you Add, Subtract, Multiply, or Divide? [Enter - + , - , * , /   :")
#operator = input()
#print("Enter the second value:  ")
#y = input()
#answer = calculate(x, y, operator)
#print(answer)

