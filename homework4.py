#1
def in_chu_so_dao_nguoc_chuoi(n):
    chuoi_so = str(n)
    if chuoi_so.startswith('-'):
        phan_so = chuoi_so[1:]
        dao_nguoc_phan_so = phan_so[::-1]
        ket_qua = "-" + dao_nguoc_phan_so
    else:
        ket_qua = chuoi_so[::-1]
    if ket_qua.startswith('-'):
        print(int(ket_qua))
    else:
        print(int(ket_qua))
try:
    so_nguyen = int(input("\nNhập vào một số nguyên n: "))
    
    print("\nKết quả (Phương pháp Chuỗi):")
    in_chu_so_dao_nguoc_chuoi(so_nguyen)
except ValueError:
    print("Lỗi: Đầu vào không phải là số nguyên hợp lệ.")

#2
def hoan_doi_xor(a, b):
    print(f"Trước khi hoán đổi: a = {a}, b = {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b    
    print(f"Sau khi hoán đổi: a = {a}, b = {b}")
    return a, b

#3
def kiem_tra_luy_thua_cua_2(n):
    if n <= 0:
        return False
    if (n & (n - 1)) == 0:
        return True
    else:
        return False
print(f"8 là lũy thừa của 2: {kiem_tra_luy_thua_cua_2(8)}")     
print(f"16 là lũy thừa của 2: {kiem_tra_luy_thua_cua_2(16)}")  
print(f"1 là lũy thừa của 2: {kiem_tra_luy_thua_cua_2(1)}")    
print(f"12 là lũy thừa của 2: {kiem_tra_luy_thua_cua_2(12)}")  
print(f"0 là lũy thừa của 2: {kiem_tra_luy_thua_cua_2(0)}")      
print(f"-4 là lũy thừa của 2: {kiem_tra_luy_thua_cua_2(-4)}") 

#4
m = int(input("Vui lòng nhập số bị chia (m): "))
n = int(input("Vui lòng nhập số chia (n): "))
if n == 0:
  print("Lỗi: Không thể chia cho số 0.")
ket_qua_lam_tron_xuong = m // n
print("\n--- KẾT QUẢ ---")
print(f"Phép chia thực tế (m / n) là: {m / n}")
print(f"Kết quả làm tròn xuống (m // n) là: {ket_qua_lam_tron_xuong}")

#5
import math
m = int(input("Vui lòng nhập số bị chia (m): "))
n = int(input("Vui lòng nhập số chia (n): "))
if n == 0:
  print("Lỗi: Không thể chia cho số 0.")
ket_qua_thuc = m / n
ket_qua_lam_tron_len = math.ceil(ket_qua_thuc)
print("\n--- KẾT QUẢ ---")
print(f"Phép chia thực tế (m / n) là: {ket_qua_thuc}")
print(f"Kết quả làm tròn xuống (m // n) là: {ket_qua_lam_tron_len}")

#6
x = int(input("Vui lòng nhập một số nguyên dương x: ")) 
if x <= 0:
  print("Lỗi: Số nhập vào phải là số nguyên dương.")
elif x % 2 == 0:
  print("Even")  # Số chẵn
else:
  print("Odd")   # Số lẻ

#7
a = input("nhập vào số nguyên thứ nhất")
b = input("nhập vào số nguyên thứ hai")
if a < 0 and b < 0 :
  print("YES")
else : 
  print("NO")

#8
a = input("Vui lòng nhập chuỗi a (gồm các chữ cái thường): ")
b = input("Vui lòng nhập chuỗi b (gồm các chữ cái thường): ")
len_a = len(a)
len_b = len(b)
ket_qua = len_a > len_b
print(str(ket_qua))

#9
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
c = int(input("Nhập số nguyên dương c: "))
if a <= 0 or b <= 0 or c <= 0:
  print("Lỗi: Cả ba số phải là số nguyên dương.")
if (a + b > c) and (a + c > b) and (b + c > a):
  print("Yes") 
else:
  print("No") 

#10


