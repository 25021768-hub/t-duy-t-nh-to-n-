n = int(input("Nhập số nguyên dương n: "))
tong = 0
temp = n

while temp > 0:
    tong += temp % 10    # Lấy chữ số cuối cùng và cộng vào tổng
    temp //= 10          # Bỏ chữ số cuối cùng

print("Tổng các chữ số của", n, "là:", tong)