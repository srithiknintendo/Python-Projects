numbers = [1,2,3,4,5]
squares = []
for num in numbers:
    squares.append(num*num)

squa_comp = [num*num for num in numbers]
print(squa_comp)
even_numbers = [num for num in numbers if num %2 ==0]
print(even_numbers)



squares_dict = {}
for num in numbers : 
    squares_dict[num] = (num*num)

squares_dict_comp = {num:num*num for num in numbers}
print(squares_dict_comp)
even_squares_dict = {num:num*num for num in numbers if num%2}
print(even_squares_dict)


def double(x):
    return x*2
doubled_num =   list(map(double,number))
tripled_num =   list(map(lambda x:x*3,numbers))



names = ["Aman","Aarav","Srithik"]
score = [67,89,45]
combined = list(zip(names, score))
print(combined)
student_mark = list(zip(names.score))
print(student_mark)


age = 15
if age<18:
    print("you are under 18")
    exit()