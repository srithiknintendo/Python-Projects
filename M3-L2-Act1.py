def total_calc(bill_amount, tip_perc=10):
    """Function to calculate total bill including tip"""

    total = bill_amount *(1+0.01*tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

total_calc(150)
total_calc(150,20)