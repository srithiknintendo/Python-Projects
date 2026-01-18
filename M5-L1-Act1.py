class Car:
    def __init__(self,brand ,color ,model ):
        self.brand = brand
        self.color = color
        self.model = model
    def details(self):
        print(f"Brand:{self.brand} \n Color:{self.color}\nModel:{self.model}")
    def start(self):
        print("vroom")
    def stop():
        print("screeech")

bmw = Car("BMW","Blue","M5")

bmw.details()