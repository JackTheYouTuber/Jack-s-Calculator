from tkinter import *

root = Tk()
root.title("Entry_Example")

entryWiget = Entry(root, width=50, bg="blue", fg="cyan", borderwidth=9)
entryWiget.pack()

def nameTakerAndDisplayer():
    Hello = "Hello there, " + entryWiget.get() +"."
    nameLabel = Label(root, text=Hello, fg="cyan")
    nameLabel.pack()

buttonWiget = Button(root, text="Enter", padx=50, pady=50, fg="cyan", bg="blue", command=nameTakerAndDisplayer)
buttonWiget.pack()

root.mainloop()
