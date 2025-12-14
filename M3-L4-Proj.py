def check_age(age):
    try:
        
        if age == int(age):
            raise ValueError(" Age should be integer")
        if age<0:
            raise ValueError(" age cannot be negative")
        if age % 2==0:
            print(f"{age} is a even number")
        else:
            print(f"{age} is an odd number")
    except ValueError as e:
        print(f"Age should be integer or invalid age entered {e}")
user_input = input("Enter your age:")
check_age(user_input)