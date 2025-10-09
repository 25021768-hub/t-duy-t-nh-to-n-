a = input("Nhập chuỗi a: ")
b = input("Nhập chuỗi b: ")

result = ""
i = 0
while i < len(a):
    found = False
    
    if a[i:i+len(b)] == b:
        found = True
    if found:
        i += len(b)  
    else:
        result += a[i]
        i += 1

print("Chuỗi a sau khi xóa chuỗi b:", result)