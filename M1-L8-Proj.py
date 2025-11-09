a = int(input("Enter value 1: "))
b = int(input("Enter value 2: "))
c = int(input("Enter value 3: "))

print("Before swapping:")
print("a =", a, ", b =", b, ", c =", c)

a = a + b + c   
b = a - (b + c) 
c = a - (b + c) 
a = a - (b + c) 

print("After swapping:")
print("a =", a, ", b =", b, ", c =", c)
