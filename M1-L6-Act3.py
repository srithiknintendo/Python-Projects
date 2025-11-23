height = float(input("Enter your height in cm"))
weight = float(input("Enter your weight in kg"))

BMI = weight / (height/100)**2
if BMI <=18.4:
    print("YOU ARE UNDER WEIGHT")
elif BMI <=24.9:
    print("you are healthy ")
elif BMI <=29.9:
    print("YOU ARE OVER WEIGHT")
elif BMI <=34.9:
    print("YOU ARE SEVERELY OVER WEIGHT")
elif BMI <=39.9:
    print("YOU ARE OBESE, GO RUNING")
else:
    print("YOU ARE SEVERELY OBESE, GO RUNING")