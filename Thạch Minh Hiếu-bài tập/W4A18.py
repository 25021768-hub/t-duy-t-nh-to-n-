a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

min_ab = min(a, b)
print("Các ước chung của", a, "và", b, "là:")
for i in range(1, min_ab + 1):
    if a % i == 0 and b % i == 0:
        print(i)