import random
number = str(random.randint(0,9))
print("I will generate a number from one to nine, and you will have to guess a number")
print("The game will end when you get 1 hero")
while True:
    guess = input("Give me your best guess \n")
    if number == guess:
        print("YOU WIN")
        print("The number was", number)
        break
    else:
        print("Your guess wasn't quite right, TRY AGAIN. \n")