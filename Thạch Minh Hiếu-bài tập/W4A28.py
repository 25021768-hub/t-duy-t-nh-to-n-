s = input("Nhập chuỗi: ")

count = 0
in_word = False

for i in range(len(s)):
    if s[i] != ' ' and not in_word:
        count += 1
        in_word = True
    elif s[i] == ' ':
        in_word = False

print("Số từ trong chuỗi là:", count)