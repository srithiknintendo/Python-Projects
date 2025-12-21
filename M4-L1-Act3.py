newlist = [4,5,1,2,9,7,10,8]
print("og list",newlist)
count = 0
for i in newlist:
    count+=i
avg = count/len(newlist)
print("sum",count)
print("average",avg)
newlist.sort()
print("smallest", newlist[0])
print("largest ", newlist[0])
