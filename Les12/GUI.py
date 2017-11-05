from tkinter import *

def clicked():
    label['text'] = entry.get()

root = Tk()
label = Label(master=root, text='Hello World', background='Yellow',
foreground='blue', font=('Helvetica', 16, 'bold italic'), width=14, height=3)
label.pack()

button1 = Button(master=root, text='Druk hier', command=clicked)
button1.pack(pady=10)

button2 = Button(master=root, text='Button2')
button2.pack(side=LEFT, pady=10)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)
root.mainloop()
