from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

def calculate_age():
    name = entry_name.get()
    day = int(entry_day.get())
    month = int(entry_month.get())
    year = int(entry_year.get())

    today = date.today()
    age = today.year - year

    message = "Hello " + name + "! Your age is " + str(age) + " years."
    result_label.config(text=message)

Label(root, text="Name:", bg="lightblue").pack()
entry_name = Entry(root)
entry_name.pack()

Label(root, text="Day:", bg="lightgreen").pack()
entry_day = Entry(root)
entry_day.pack()

Label(root, text="Month:", bg="lightyellow").pack()
entry_month = Entry(root)
entry_month.pack()

Label(root, text="Year:", bg="lightpink").pack()
entry_year = Entry(root)
entry_year.pack()

Button(root, text="Calculate Age", command=calculate_age, bg="orange").pack(pady=10)

result_label = Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()