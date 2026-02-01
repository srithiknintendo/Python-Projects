class Reverse:
    def __init__(self, s=""):
        self.s = s

    def get_reverse(self):
        return self.s[::-1]


# Take input from the user
user_input = input("Enter a string: ")

# Create object of the class
obj = Reverse(user_input)

# Print reversed string
print("Reversed string:", obj.get_reverse())
