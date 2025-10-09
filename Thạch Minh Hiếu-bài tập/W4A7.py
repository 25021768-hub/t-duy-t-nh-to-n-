def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n
n = int(input("Nhập vào số nguyên dương n (n ≥ 2): "))
if n < 2:
    print("Vui lòng nhập số nguyên lớn hơn hoặc bằng 2.")
else:
    print("Ước số nguyên tố lớn nhất của", n, "là:", largest_prime_factor(n))
