print("Select your ride:")
print("1.Bike")
print("2.Car")
Choice = int(input("Enter your choice:"))

if Choice == 1 :
    print("Selct your bike:")
    print("1.Scooty")
    print("2.Scooter")
    
    Choice1 = int(input("Enter your choice:"))
    
    if Choice1 == 1 :
        print("You have selected Scooty")
    else:
        print("You have selected Scooter")

elif Choice == 2 :
    print("Selct your car:")
    print("1.Sedan")
    print("2.XUV")

    Choice2 = int(input("Enter your choice:"))
    
    if Choice2 == 1 :
        print("You have selected Sedan")
    else:
        print("You have selected XUV")
        
else:
    print("Wrong choice")
