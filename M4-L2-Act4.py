weather = (1,0,1,0,1,0,1)
sun = 0
rain = 0
for i in range(0,7):
    if (weather[i]==0):
        rain+=1
    else:
        sun+=1

if (sun>rain):
    print("good")
else:
    print("bad")