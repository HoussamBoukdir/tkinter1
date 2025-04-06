from tkinter import *

master = Tk()
master.title("Mini Project - Languages")

Label(master, text="Select a language:").grid(row=0, column=0, columnspan=2)

Lb = Listbox(master)
Lb.insert(0, 'Python')
Lb.insert(1, 'Java')
Lb.insert(2, 'C++')
Lb.insert(3, 'JavaScript')
Lb.insert(4, 'Other')
Lb.grid(row=1, column=0, columnspan=2)

Label(master, text='First Name:').grid(row=2, column=0)
Label(master, text='Last Name :').grid(row=3, column=0)

e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=2, column=1)
e2.grid(row=3, column=1)

def submit():
    print("First Name:", e1.get())
    print("Last Name:", e2.get())
    selected = Lb.curselection()
    if selected:
        print("Language:", Lb.get(selected[0]))

Button(master, text="Submit", command=submit).grid(row=4, column=0, columnspan=2)

master.mainloop()
