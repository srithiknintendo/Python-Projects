class Flashcards:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
Flash = []
print("welcome to flashcards application")
while(True):
    word = input("enter the word")
    meaning = input("enter the definition")
    Flash.append(Flashcards(word, meaning))
    option = int(input("enter 0(to stop) or 1(for more flashcards)"))
    if(option):
        break
print("\nYour Flashcards")
for i in Flash:
    print(">",i)