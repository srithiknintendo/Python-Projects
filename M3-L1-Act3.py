def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2
print("choose your operation")
print("a for addition")
print("s for subtraction")
print("m for multiplication")
print("d for division")
oper  = str(input("enter your   operation:"))
num1  = int(input("enter your first  term:"))
num2  = int(input("enter your second term:"))

if   oper == "a" :
    print(num1, "+",num2,"=",addition(num1, num2))
elif oper == "s" :
    print(num1, "-",num2,"=",subtraction(num1, num2))
elif oper == "m" :
    print(num1, ".",num2,"=",multiplication(num1, num2))
elif oper == "d" :
    print(num1, "÷",num2,"=",division(num1, num2))
else:
    print("error")