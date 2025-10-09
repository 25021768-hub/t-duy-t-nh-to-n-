import math
def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua = giai_thua * i   
    return giai_thua
def nhap_so_nguyen_hop_le():
    while True:
        try:
            n = int(input("Vui lòng nhập một số nguyên n (0 < n < 100): "))           
            if 0 < n < 100:
                return n
            else:
                print("Lỗi: Số n phải lớn hơn 0 và nhỏ hơn 100. Vui lòng thử lại.")        
        except ValueError:
            print(" Lỗi: Đầu vào không hợp lệ. Vui lòng chỉ nhập số nguyên.")
so_n = nhap_so_nguyen_hop_le()
ket_qua = tinh_giai_thua(so_n)
print(f" Đã nhập n = {so_n}")
print(f" Giai thừa của {so_n} (tức là {so_n}!) là: {ket_qua}")