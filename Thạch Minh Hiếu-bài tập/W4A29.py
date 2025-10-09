chuoi_nhap_vao = input("nhập vào 3 số nguyên, mỗi số cách nhàu bằng dấu , ")
danh_sach_so = [int(so.strip()) for so in chuoi_nhap_vao.split(',')]
tong = sum(danh_sach_so)
print("Danh sách số:", danh_sach_so) 
print("Tổng:", tong)                  