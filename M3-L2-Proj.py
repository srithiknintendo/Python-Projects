def shutdown(yeno):
    if yeno == "yes":
        print("shutdown")
    elif yeno == "no":
        print("awake")
    else:
        print("sorry")
yeno = str(input("Enter yes or no:"))
shutdown(yeno)