s = input("Nhập chuỗi: ")

hoa = 0
thuong = 0
so = 0

for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        hoa += 1
    elif 'a' <= s[i] <= 'z':
        thuong += 1
    elif '0' <= s[i] <= '9':
        so += 1

print("Số ký tự in hoa:", hoa)
print("Số ký tự in thường:", thuong)
print("Số ký tự số:", so)