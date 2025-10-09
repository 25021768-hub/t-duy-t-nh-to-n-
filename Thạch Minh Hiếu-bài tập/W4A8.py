def is_palindrome(n):
    return str(n) == str(n)[::-1]
def reverse_number(n):
    return int(str(n)[::-1])
def reverse_add_palindrome(n):
    steps = 0
    while not is_palindrome(n):
        reversed_n = reverse_number(n)
        n = n + reversed_n
        steps += 1
    return steps, n

n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
else:
    steps, palindrome = reverse_add_palindrome(n)
    print(f"Số bước: {steps}")
    print(f"Giá trị palindrome: {palindrome}")
