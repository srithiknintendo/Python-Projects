markONE     = int (input())
markTWO     = int (input())
markTHREE   = int (input())
markFOUR    = int (input())
markFIVE    = int (input())

total = markONE + markTWO + markTHREE + markFOUR + markFIVE 
tot =total /5

if      (91 <  tot) and (tot >100):
    print("YOUR GRADE IS A1")
elif    (81 <  tot) and (tot > 91):
    print("YOUR GRADE IS A2")
elif    (71 <  tot) and (tot > 81):
    print("YOUR GRADE IS B1")
elif    (61 <  tot) and (tot > 71):
    print("YOUR GRADE IS B2")
elif    (51 <  tot) and (tot > 61):
    print("YOUR GRADE IS C1")
elif    (41 <  tot) and (tot > 51):
    print("YOUR GRADE IS C2")
elif    (31 <  tot) and (tot > 41):
    print("YOUR GRADE IS D1")
elif    (21 <  tot) and (tot > 31):
    print("YOUR GRADE IS D2")
elif    (11 <  tot) and (tot > 21):
    print("YOUR GRADE IS E1")
else :
    print("YOUR GRADE IS E2")