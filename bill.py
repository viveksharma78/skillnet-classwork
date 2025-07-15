bill_amount = float(input("Enter total bill amount: "))
friends = int(input("Enter number of friends to divide: "))

if friends == 0:
    print("Number of friends cannot be 0.")
else:
    per_person = bill_amount / friends
    print(f"Each person pays: ₹{per_person:.2f}")

    tip_percent = float(input("Enter tip percent (10 to 35): "))
if 10 <= tip_percent <= 35:
        tip_amount = (bill_amount * tip_percent) / 100
        total_with_tip = bill_amount + tip_amount
        print(f"Tip amount: ₹{tip_amount:.2f}")
        print(f"Total bill with tip: ₹{total_with_tip:.2f}")
else:
         print("Tip percent must be between10and35.")