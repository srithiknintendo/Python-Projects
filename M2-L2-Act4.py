s = str(input("Enter your sentence:"))
total = 1
for i in range(len(s)):
    if(s[i] == ' ' ):
        total = total + 1
print(total)