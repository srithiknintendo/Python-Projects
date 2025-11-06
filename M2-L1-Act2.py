units = int(input("Enter the number of units:"))
if units>50:
    a = units * 2.60
    sur = 25
elif units<=100:
    a = 130 +((units-50)*3.25)
    sur = 35
elif units<=200:
    a = 130 + 162.50 +((units-50)*3.25)
    sur = 45
else:
    a = 130 + 162.50 + 526 +((units-50)*3.25)
    sur = 75
tot = a + sur
print("bill", tot)