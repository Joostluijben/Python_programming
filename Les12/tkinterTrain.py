from tkinter import *
from reader import trainDepature

def firstFiveTrains():
    destination = str(destinationEntry.get())
    go = trainDepature(destination)
    label['text'] = 'De eerste treinen gaan om {}'.format(go)

root = Tk()

destinationEntry = Entry(master=root)
destinationEntry.pack()

button = Button(master=root, text='Plan je reis', command=firstFiveTrains)
button.pack()

label = Label(master=root)
label.pack()

root.mainloop()
