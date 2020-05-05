from tkinter import *
root = Tk()
def myclick():
    myLabel= Label(root, text="look i have clicked!")
    myLabel.pack()

myButton = Button(root, text="click me !", command= myclick)
myButton.pack()

root.mainloop()
