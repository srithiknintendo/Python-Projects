rows = int(input("Enter number of rows: "))

print("Mirror Right-Angled Triangle")

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()