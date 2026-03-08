from tkinter import*

window = Tk()
window.title("Hi")
window.geometry("10000x100")


def handle_keypress(event):
    """zzzzzzzzzzzzz"""
    print(event.char)

window.bind("<Key>",handle_keypress)

def handle_click(event):
    print("\nb was clicked")

button = Button(text='click me')
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()