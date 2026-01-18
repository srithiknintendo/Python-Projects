class Dog:
    animal = "Dog"
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    def print_details(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Colour:", self.colour)
dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")
print("Dog 1 Details:")
dog1.print_details()

print("Dog 2 Details:")
dog2.print_details()
