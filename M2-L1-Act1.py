med = input("Enter Y if you have a medical cause or N:")
att = int(input("Enter the students attendance:"))

if med=="Y":
    print("Allow the student to class")
else :
    if att >= 75:
        print("Allow the student to class")
    else:
        print("Don't allow the student to class")
