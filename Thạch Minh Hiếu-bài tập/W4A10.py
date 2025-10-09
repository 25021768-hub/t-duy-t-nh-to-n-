def collatz_length(x):
    length = 1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        length += 1
    return length

n = int(input("Nhập số nguyên dương n: "))

max_length = 0
result_x = 1

for i in range(1, n+1):
    current_length = collatz_length(i)
    if current_length > max_length:
        max_length = current_length
        result_x = i

print(result_x, max_length)
