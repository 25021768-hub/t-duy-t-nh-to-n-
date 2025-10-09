s = input("Nhập mật khẩu: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        has_upper = True
    elif 'a' <= s[i] <= 'z':
        has_lower = True
    elif '0' <= s[i] <= '9':
        has_digit = True
    else:
        has_special = True

if has_upper and has_lower and has_digit and has_special and len(s) > 6:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")