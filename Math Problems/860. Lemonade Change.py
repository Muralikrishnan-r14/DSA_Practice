def lemonadeChange(bills):
    cnt_5, cnt_10 = 0, 0  # Track $5 and $10 bills

    for bill in bills:
        if bill == 5:
            cnt_5 += 1  # Always accept $5

        elif bill == 10:
            if cnt_5 == 0:
                return False  # Can't give change
            cnt_5 -= 1
            cnt_10 += 1  # Store $10 for future $20 bills

        else:  # bill == 20
            if cnt_10 > 0 and cnt_5 > 0:  # Prefer giving $10 + $5
                cnt_10 -= 1
                cnt_5 -= 1
            elif cnt_5 >= 3:  # Otherwise, give three $5 bills
                cnt_5 -= 3
            else:
                return False  # Not enough change

    return True  # All customers got correct change
bills = [5,5,5,10,20]
print(lemonadeChange(bills))