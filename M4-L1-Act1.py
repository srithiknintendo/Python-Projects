friends = ["raj", "rahul", "deva", "sahiba", "nidhi"]
print("1st", friends[0])
print("2nd", friends[1])
print("3rd", friends[2])
print("4th", friends[3])
print("5th", friends[4])

friends[4] = "srithik"
print("updated list", friends)
count = 1
for i in friends :
    print(f"my{count} friend is {i}")
    count = count +1

num = [0,1,2,3,4,5,6,7,8,9]
for i in num:
    print(i*i, end = " ")