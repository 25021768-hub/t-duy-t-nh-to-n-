n = int(input("Nhập số nguyên: "))
s = str(abs(n))  # chuyển số sang chuỗi, lấy trị tuyệt đối để xử lý

result = ""
count = 0

for i in range(len(s) - 1, -1, -1):
    result = s[i] + result
    count += 1
    if count % 3 == 0 and i != 0:
        result = '.' + result

if n < 0:
    result = '-' + result

print("Số sau khi phân tách:", result)