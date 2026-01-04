test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
value = int(input("Enter an integer value to check its frequency: "))
frequency = list(test_dict.values()).count(value)
print(f"The value {value} appears {frequency} time(s) in the dictionary.")