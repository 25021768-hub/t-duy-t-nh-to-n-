import math
def dem_so_chu_so_khong_string(n):
    so_duong = int(math.fabs(n))
    if so_duong == 0:
        return 1
    dem = 0
    so_hien_tai = so_duong
    while so_hien_tai > 0:
        so_hien_tai = so_hien_tai // 10   
        dem = dem + 1       
    return dem
while True:
    try:
        n = int(input("Vui lòng nhập một số nguyên n: "))
        break 

    except ValueError:
        print("Lỗi: Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
so_chu_so = dem_so_chu_so_khong_string(n)
print(f"\nSố bạn đã nhập là: {n}")
print(f"Số chữ số (trừ dấu) của số {n} là: {so_chu_so}")