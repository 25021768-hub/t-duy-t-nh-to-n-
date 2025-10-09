n = int(input("Nhập số nguyên dương n: "))
chan = 0
le = 0
temp = n

while temp > 0:
    digit = temp % 10
    if digit % 2 == 0:
        chan += 1
    else:
        le += 1
    temp //= 10

print("Số chữ số chẵn của", n, "là:", chan)
print("Số chữ số lẻ của", n, "là:", le)