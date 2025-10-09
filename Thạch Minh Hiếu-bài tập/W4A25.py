numbers = []
while True:
    num = int(input("Nhập số nguyên (nhập -1 để kết thúc): "))
    if num == -1:
        break
    numbers.append(num)

if numbers:
    print("Số lớn nhất là:", max(numbers))
    print("Số nhỏ nhất là:", min(numbers))
else:
    print("Không có số nào được nhập.")