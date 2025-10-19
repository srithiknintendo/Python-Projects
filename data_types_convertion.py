
Name        = "John Grade"
Age         = 23
is_student  = False
Height      = 1.7

print("name :", Name)
print("type of data", type(Name))

print("\nage  :", Age)
print("type of data", type(Age))

print("\nIs student :", is_student)
print("type of data", type(is_student))

print("\nHeight :", Height)
print("type of data", type(Height))


print("\n\nAfter type casting...")
Age         = str(Age)
print(Age)
Height      = int(Height)
print(Height)