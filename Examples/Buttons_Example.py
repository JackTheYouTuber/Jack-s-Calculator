from tkinter import *

root = Tk()
root.title("Buttons_Example")

def click():
    myLable = Label(root, text="Hello!", fg="cyan")
    myLable.pack()

myButton = Button(root, text="Click Me!", padx=50, pady=50, command=click, fg="cyan", bg="blue")
myButton.pack()

root.mainloop()
