def dem_so_uoc(n):
    count = 0 
    for i in range(2,n+1,2):
        if n % i == 0:
            count += 1
    return count

n = int(input("Nhập vào 1 số nguyên dương"))
if 0 < n <= 10**6:
    print("số ước chẵn là:", dem_so_uoc(n))
else :
    print("số n ko hợp lệ")