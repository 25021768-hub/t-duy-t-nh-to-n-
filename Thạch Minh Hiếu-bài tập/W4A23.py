n = int(input("Nhập n: "))

k = 0
S = 0

while True:
    if S + (k + 1) < n:
        k += 1
        S += k
    else:
        break

print("Giá trị k lớn nhất sao cho S(k) < n là:", k)
print("Tổng S(k) =", S)