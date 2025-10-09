import math

def has_unique_digits(n):
    s = str(n)
    return len(set(s)) == len(s)

n = int(input("Nhập số nguyên dương n: "))

results = []

for i in range(0, int(math.sqrt(n)) + 1):
    square = i * i
    if has_unique_digits(square):
        results.append(square)

if results:
    print(*results) 
else:
    print("(no number)")
