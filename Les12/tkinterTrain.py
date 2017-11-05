from tkinter import *
from reader import trainDepature

def reisPlanner():
    destination = trainDepature(destinationEntry.get())
    label['text'] = destination

root = Tk()

destinationEntry = Entry(master=root)
destinationEntry.pack()

button = Button(master=root, text='Druk hier', command=reisPlanner)
button.pack()

label = Label(master=root, text='test')
label.pack()

root.mainloop()
