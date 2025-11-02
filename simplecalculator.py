firstTerm  = float(input("Enter your first number:"))
print("To enter you operation choose: one of the following:")
print("For multiplication use:x")
print("For addition use      :+")
print("For soustrastion use  :-")
print("For division use      :/") 
operation   = input("Enter you operation:")
secondTerm  = float(input("Enter your second number:"))
if   operation == '+':
    print(firstTerm,"+",secondTerm,"=",firstTerm + secondTerm)
elif operation == 'x':
    print(firstTerm,"x",secondTerm,"=",firstTerm * secondTerm)
elif operation == '-':
    print(firstTerm,"-",secondTerm,"=",firstTerm - secondTerm)
elif operation == '/':
    print(firstTerm,"÷",secondTerm,"=",firstTerm / secondTerm)
else:
    print("operation sign not found")