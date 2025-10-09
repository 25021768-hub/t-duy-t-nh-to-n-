A = int(input("Nhập số nguyên dương A: "))

f1, f2 = 1, 1
fib_max = 1

while f2 <= A:
    fib_max = f2
    f1, f2 = f2, f1 + f2

print("Số Fibonacci lớn nhất không vượt quá", A, "là:", fib_max)