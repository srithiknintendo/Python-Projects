from tkinter import *

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

label_desc = Label(root, text="Enter two numbers to calculate their product", bg="#AED6F1")
label_desc.pack(pady=5)

label1 = Label(root, text="Enter first number:", bg="#A3E4D7")
label1.pack()

entry1 = Entry(root, bg="#F9E79F")
entry1.pack()

label2 = Label(root, text="Enter second number:", bg="#A3E4D7")
label2.pack()

entry2 = Entry(root, bg="#F9E79F")
entry2.pack()

def calculate():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result = n1 * n2
    text_box.delete("1.0", END)
    text_box.insert(END, str(result))

button = Button(root, text="Calculate Product", command=calculate, bg="#F5B7B1")
button.pack(pady=5)

text_box = Text(root, height=2, width=20, bg="#D7BDE2")
text_box.pack()

root.mainloop()