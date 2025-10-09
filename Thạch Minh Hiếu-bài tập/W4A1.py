def tinh_tong_for(n):
    if n <= 0 or n > 1000:
        return    
    tong = 0   
    for i in range(1, n + 1):
        tong += i        
    return tong
n_input = int(input("Nhập số nguyên dương n (n <= 1000): "))
ket_qua = tinh_tong_for(n_input)   
print(f"Tổng các số từ 1 đến {n_input} là: {ket_qua}")