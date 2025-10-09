x = int(input("Nhập vào số nguyên dương thứ nhất:"))
y = int(input("Nhập vào số nguyên dương thứ hai :"))
def tong_cua_2_so(num):
    total = 0
    for i in range(1, num//2 + 1):
        if num % i == 0:
            total += i
    return total
tong_x = tong_cua_2_so(x)
tong_y = tong_cua_2_so(y)
if tong_x == y and tong_y == x:
    print("True")
else:
    print("False")
