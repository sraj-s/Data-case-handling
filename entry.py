from tkinter import *
root = Tk()
e= Entry(root, width= 50)
e.pack()
e.insert(0, "Enter your name")

def myclick():
    hello= "Hello" + e.get()
    myLabel= Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter your name !", command= myclick)
myButton.pack()

root.mainloop()
