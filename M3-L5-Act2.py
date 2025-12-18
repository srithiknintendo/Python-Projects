import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors)")
    poss_action = ["rock","paper","scissors"]
    comp_action = random.choice(poss_action)
    print("You chose", user_action,"and the computer chose",comp_action)
    if   user_action =="rock":
        if comp_action == "scissors":
            print("rock smashes scissors you win")
        else:
            print("paper covers rock you lose")
    elif user_action =="paper":
        if comp_action == "rock":
            print("paper covers rock you win")
        else:
            print("scissors cut paper you lose")
    elif user_action =="scissors":
        if comp_action == "Paper":
            print("scissors cut paper you win")
        else:
            print("rock smashes scissors you lose")
    play_ag = input("Play again?(y/n)")
    if play_ag=="n":
        break