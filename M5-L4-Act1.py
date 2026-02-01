class Person:
    def __init__(self,name,age,num):
        self.name = name
        self.age  = age
        self.num  = num
        print(f"{self.name}Object has been created")
    def display(self):
        print(f"""
        User Information :-
            name : {self.name}
            age  : {self.age}
            num  : {self.num}
        """)
    def getNumber(self):
        print(f"(using getter function)Your phone is {self.num}")
    def setNumber(self, newNumber):
        print(f"old num was {self.num}")
        self.num = newNumber
        print(f"(using setter function) new num is {self.num}")
obj1 = Person("ram",24,+32455189868)
obj1.display()
obj1.getNumber()
obj1.setNumber(12345678912345678901234567890)