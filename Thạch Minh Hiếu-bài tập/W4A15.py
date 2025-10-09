total_animals = int(input("Nhập tổng số con: "))
total_legs = int(input("Nhập tổng số chân: "))

found = False
for chickens in range(total_animals + 1):
    dogs = total_animals - chickens
    if 2 * chickens + 4 * dogs == total_legs:
        print("Số gà:", chickens)
        print("Số chó:", dogs)
        found = True
        break

if not found:
    print("invalid")