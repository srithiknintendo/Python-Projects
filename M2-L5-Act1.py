rows =int(input("Enter the number of rows"))
print("Half pyramid of stars(*)")
for i in range (1,rows + 1):
    for j in range(i):
        print("*",end="")
    print()