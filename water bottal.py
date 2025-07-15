total_bottles = int(input("Enter total water bottles: "))
bottles_per_day = int(input("Enter bottles you drink per day: "))

day = 1
while total_bottles > 0:
    if total_bottles >= bottles_per_day:
        print(f" {day} {bottles_per_day} bottles. {total_bottles - bottles_per_day} left.")
        total_bottles -= bottles_per_day
    else:
        print(f"{day}:{total_bottles} bottle(s). 0 left.")
        total_bottles = 0
    day += 1

print("# No more bottles left!")