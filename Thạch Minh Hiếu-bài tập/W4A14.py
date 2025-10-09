def ucln(m, n):
    while n != 0:
        m, n = n, m % n
    return m

m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

print("Ước chung lớn nhất của", m, "và", n, "là:", ucln(m, n))