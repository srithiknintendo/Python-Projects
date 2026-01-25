class Animal:
    def __init__(self, name):
        self.name =name
        print("object created")
    def speak(self):
        print(f"{self.name}is speaking")
    def walk(self):
        print(f"{self.name}is walking")

class dog(Animal):
    def __init__(self, breed, name):
        self.breed = breed
        super.__innit__(name)
    def display(self):
        print(f"{self.name}\n{self.breed}") 
class cat(Animal):
    def __init__(self, breed, name):
        self.breed = breed
        super.__init__(name)
    def display(self):
        print(f"{self.name}\n{self.breed}") 
dog1 = dog("golden retriever", "Kai")
cat1 = cat("golden cat", "Zane")
dog1.speak()
cat1.display()
