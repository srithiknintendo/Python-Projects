n = abs(int(input("Enter a number: ")))
c = 1

while n >= 10:
    n //= 10
    c += 1

print(c)
