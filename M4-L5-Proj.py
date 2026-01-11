# Task 1: Odd and Even numbers below a given number
num = int(input("Enter a number: "))

odd_numbers = [i for i in range(num) if i % 2 != 0]
even_numbers = [i for i in range(num) if i % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

# Task 2: Capitalize first letter of each fruit
fruits = ["apple", "banana", "mango", "orange", "grapes"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits list:", fruits)
print("Capitalized fruits list:", capitalized_fruits)
