n = int(input("Nhập số nguyên dương n: "))

if n > 0 and (n & (n - 1)) == 0:
    print(n, "là số dạng 2^k")
else:
    print(n, "không phải là số dạng 2^k")