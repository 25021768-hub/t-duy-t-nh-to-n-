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
a = int(input("nhập vào số nguyên :"))
b = int(input("nhập vào số nguyên :"))
c = int(input("nhập vào số nguyên :"))
d = int(input("nhập vào số nguyên :"))
max = max(a,b,c,d)
print(max)

#11
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
c = int(input("Nhập số nguyên dương c: "))
if a <= 0 or b <= 0 or c <= 0:
  print("Lỗi: Cả ba số phải là số nguyên dương.")
if (a + b < c) and (a + c < b) and (b + c < a):
    print("không phải tam giác")
elif (a == b) or (a == c) or (b == c):
    print("đây là tam giác cân")
elif (a == b == c) :
    print("đây là tam giác đều")
else :
    print("đây là tam giác thường")

#12
a = int(input("nhập vào một năm :"))
if a % 4 == 0 and a % 100 != 0:
  print("YES")
elif a % 400 == 0 :
  print("YES")
else : 
  print("NO")

#13
a = int(input("nhập số kWh điện tiêu thụ :"))
if 0 <= a <= 50 :
    print ("Số tiền điện là : ", a*1500, "đồng")
if 51 <= a < 100 : 
    print("Số tiền điện là : ", (a-50)*2000 + 50*1500 , "đồng")
if a >= 100 :
    print("Số tiền điện là : ", (a-100)*3000 + 50*2000 + 50*1500, "đồng")

#14
import math
a = float(input("Nhập vào hệ số a"))
b = float(input("Nhập vào hệ số b"))
if a == 0:
  if b == 0:
    print("Vô số nghiệm")
  else:
    print("Vô nghiệm")
else:
  x = -b / a
  x_lam_tron = round(x, 2)
  print(f"Nghiệm của phương trình là: {x_lam_tron}")

#15
a = float(input("Nhập vào điểm trung bình"))
if a >= 8.0 :
    print("Học sinh giỏi")
elif 6.5 <= a < 8.0 :
    print("Học sinh khá")
elif 5.0 <= a <= 6.5 : 
    print("Học sinh trung bình")
else :
    print("Học sinh yếu")

#17
def lam_tron_thu_cong(so_thuc_str):
  x = float(so_thuc_str)
  lam_tron_xuong = int(x)
  if x < 0 and x != lam_tron_xuong:
      lam_tron_xuong = lam_tron_xuong - 1
  if x == int(x):
      lam_tron_len = int(x)
  elif x > 0:
      lam_tron_len = int(x) + 1
  else: 
      lam_tron_len = int(x)
  if x >= 0:
      lam_tron_gan_nhat = int(x + 0.5)
  else: 
      lam_tron_gan_nhat = int(x - 0.5)
  return f"{lam_tron_len} {lam_tron_xuong} {lam_tron_gan_nhat}"
so_nhap_vao = input("Nhập vào một số thực: ")
ket_qua = lam_tron_thu_cong(so_nhap_vao)
print(ket_qua)

#18
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
c = int(input("Nhập số nguyên dương c: "))
if a <= 0 or b <= 0 or c <= 0:
  print("Lỗi: Cả ba số phải là số nguyên dương.")
if (a + b < c) and (a + c < b) and (b + c < a):
    print("không phải tam giác")
elif (a == b) or (a == c) or (b == c):
    print("đây là tam giác cân")
elif (a == b == c) :
    print("đây là tam giác đều")
else :
    print("đây là tam giác thường")




    








