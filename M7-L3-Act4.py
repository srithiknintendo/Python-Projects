from tkinter import*
import random
root = Tk()
root.title('Rock paper scissors')
root.geometry("400x400")
root.config(bg='#f0f0f0')
choices = ["Rock","Paper","Scissors"]
user_label = Label(root,text = "Your choice:",font = ("Arial",14))
user_label.pack(pady = 20)
result_label = Label(root,text = "",font = ("Arial",16,"bold"),fg = "blue")
result_label.pack(pady = 20)
comp_label = Label(root,text = "",font = ("Arial",14))
comp_label.pack(pady = 10)
def play(user_choice):
    comp_choice = random.choice(choices)
    comp_label.config(text = f"Computer Chose:{comp_choice}")

    if user_choice == comp_choice:
        result = ("Its a tie")
    elif (user_choice == "Rock" and comp_choice == "Scissors") or\
         (user_choice == "Paper" and comp_choice == "Rock") or\
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You win"
    else:
        result = "You Lose!"

    result_label.config(text=result)

# Button frame
btn_frame = Frame(root)
btn_frame.pack(pady=20)

# Buttons
rock_btn = Button(btn_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = Button(btn_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = Button(btn_frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Run the window
root.mainloop()
