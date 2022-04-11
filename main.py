from tkinter import *


root = Tk()

# Lable declaration
mainLable = Label(root, text="Jack's Calculator", padx=10, pady=5)


#Button declaration
simpleMathButton = Button(root, text="Simple Math", padx=10 , pady=5)
complexMathButton = Button(root, text="Complex Math", padx=10 , pady=5)
graphMathButton = Button(root, text="Graph Math", padx=10 , pady=5)

#Button initalization
simpleMathButton.grid(row=1,column=0)
complexMathButton.grid(row=2,column=0)
graphMathButton.grid(row=3,column=0)

# Lable initalization
mainLable.grid(row=0,column=0)

root.mainloop()
