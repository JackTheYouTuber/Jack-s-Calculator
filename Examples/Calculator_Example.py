from tkinter import *

root = Tk()
root.title("Calculator_Example")

Text_Field = Entry(root, width=35, borderwidth=5)
Text_Field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(num):
    current_text = Text_Field.get()
    Text_Field.delete(0, END)
    Text_Field.insert(0, str(current_text) + str(num))

def button_clear():
    Text_Field.delete(0, END)

def button_add():
    first_number = Text_Field.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    Text_Field.delete(0, END)

def button_subtract():
    first_number = Text_Field.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    Text_Field.delete(0, END)

def button_multiply():
    first_number = Text_Field.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    Text_Field.delete(0, END)

def button_divide():
    first_number = Text_Field.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    Text_Field.delete(0, END)


def button_equal():
    second_number = Text_Field.get()
    Text_Field.delete(0, END)
    if math == "addition":
        Text_Field.insert(0, f_num + int(second_number))
    if math == "subtraction":
        Text_Field.insert(0, f_num - int(second_number))
    if math == "multiplication":
        Text_Field.insert(0, f_num * int(second_number))
    if math == "division":
        Text_Field.insert(0, f_num / int(second_number))



# Define Buttons

# Number Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))

# Symbol Buttons
button_adder_i = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract_i = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply_i = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide_i = Button(root, text="/", padx=41, pady=20, command=button_divide)
button_equal_i = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear_i = Button(root, text="AC", padx=84, pady=20, command=button_clear)


# Put Buttons On Screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear_i.grid(row=4, column=1, columnspan=2)
button_adder_i.grid(row=5, column=0)
button_equal_i.grid(row=5, column=1, columnspan=2)

button_subtract_i.grid(row=6, column=0)
button_multiply_i.grid(row=6, column=1)
button_divide_i.grid(row=6, column=2)

# Run Everything

root.mainloop()
