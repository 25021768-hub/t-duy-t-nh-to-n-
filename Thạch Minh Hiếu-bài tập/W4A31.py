s = input("Nhập chuỗi: ")

tong = 0

for i in range(len(s)):
    if '0' <= s[i] <= '9':
        tong += int(s[i])

print("Tổng các ký tự số trong chuỗi là:", tong)