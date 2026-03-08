from tkinter import*
window = Tk()

def handle_keypress(event):
    """XXXXXX"""
    print(event.char)

window.bind("<Key>",handle_keypress)

window.mainloop()