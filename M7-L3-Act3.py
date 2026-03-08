from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry("10000x200")
def msg():
    messagebox.showwarning("no ","virus")
button = Button(root,text='click me',command=msg)

button.place(x=40,y=80)
root.mainloop()