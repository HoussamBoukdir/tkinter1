from tkinter import *

master = Tk()

Lb = Listbox(master)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(3, 'JSCRIPT')
Lb.insert(4, 'Any other')
Lb.grid(row=0, column=0, columnspan=2)  

Label(master, text='First Name:').grid(row=1, column=0)
Label(master, text='Last Name:').grid(row=2, column=0)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

master.mainloop()
