def calculate_savings(X, N):
    rate = 0.007  
    amount = X * ((1 + rate) ** N)
    return int(amount)  
X = float(input("Nhập số tiền gửi ban đầu (đồng): "))
N = int(input("Nhập số tháng gửi: "))
print("Số tiền sau", N, "tháng là:", calculate_savings(X, N), "đồng")
