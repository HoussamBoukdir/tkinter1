from tkinter import *

master = Tk()
master.title("Mini Project - Languages")
master.configure(bg="#f0f0f0")  


Label(master, text="Select a language:", bg="#f0f0f0", fg="#333").grid(row=0, column=0, columnspan=2, pady=(10, 0))


Lb = Listbox(master, bg="white", fg="black", selectbackground="#007acc", selectforeground="white")
Lb.insert(0, 'Python')
Lb.insert(1, 'Java')
Lb.insert(2, 'C++')
Lb.insert(3, 'JavaScript')
Lb.insert(4, 'Other')
Lb.grid(row=1, column=0, columnspan=2, pady=(0, 10), padx=10)


Label(master, text='First Name:', bg="#f0f0f0", fg="#333").grid(row=2, column=0, sticky='e', padx=5)
Label(master, text='Last Name :', bg="#f0f0f0", fg="#333").grid(row=3, column=0, sticky='e', padx=5)


e1 = Entry(master, bg="white", fg="black")
e2 = Entry(master, bg="white", fg="black")
e1.grid(row=2, column=1, padx=5, pady=2)
e2.grid(row=3, column=1, padx=5, pady=2)


def submit():
    print("First Name:", e1.get())
    print("Last Name:", e2.get())
    selected = Lb.curselection()
    if selected:
        print("Language:", Lb.get(selected[0]))

Button(master, text="Submit", command=submit, bg="#007acc", fg="white", activebackground="#005f99").grid(
    row=4, column=0, columnspan=2, pady=10
)

master.mainloop()
