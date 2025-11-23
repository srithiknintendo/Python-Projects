num = int(input("Enter a decimal number: "))
binary = ""


n = num


for i in range(32):
    if n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2


print("Binary of", num, "is:", binary)