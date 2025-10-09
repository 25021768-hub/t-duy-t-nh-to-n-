A = float(input("Nhập A: "))

S = 0
n = 1

while S <= A:
    S += 1 / n
    n += 1

print("Giá trị n nhỏ nhất sao cho tổng > A là:", n - 1)