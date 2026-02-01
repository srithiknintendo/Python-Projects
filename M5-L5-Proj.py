class BMW:
    def fuel_type(self):
        print("BMW uses Petrol")

    def max_speed(self):
        print("BMW max speed is 250 km/h")


class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Petrol")

    def max_speed(self):
        print("Ferrari max speed is 340 km/h")


# Polymorphism in action
def car_details(car):
    car.fuel_type()
    car.max_speed()


# Create objects
bmw = BMW()
ferrari = Ferrari()

# Calling the same function with different objects
car_details(bmw)
car_details(ferrari)
