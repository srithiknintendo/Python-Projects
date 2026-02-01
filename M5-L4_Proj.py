class Animal:
    def __init__(self,name):
        print(f"{name} obj is created")
    def speak(self):
        print("speaking")
class dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("Woof Woof")
class cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("miaul")
dog1 = dog("Buddy")
cat1 = cat("whis")
dog1.speak()
cat1.speak()