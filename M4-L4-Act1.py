listVar = ['a','b','c']
print(listVar)
setVar = {'a','b','c'}
print(setVar)

a = {1,2,3}
b = {3,4,5}

#UNION
print(a|b)
print(a.union(b))

#intersection
print(a & b)
print(a.intersection(b))

#difference
print(a-b)
print(a.difference(b))


numbers = [10,20,30,40]
print(numbers)

#OPERATION
numbers.append(55)
print(numbers)

numbers.insert(1,15)#num.insert(index_value,value)
print(numbers)

numbers.remove(20)
print(numbers)

numbers.pop(2)#num.pop(index_value)
print(numbers)

numbers.pop()#num.pop(index_value)
print(numbers)

for i in numbers : 
    print("number is :", i)
