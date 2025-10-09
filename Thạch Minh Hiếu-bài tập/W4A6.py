import sys
import math

def la_so_nguyen_to(n):
    if n < 2:
        return False
    can_bac_hai = math.isqrt(n)
    for i in range(2, can_bac_hai + 1):
        if n % i == 0:
            return False
    return True

def tinh_tong_so_nguyen_to(a, b):
    tong = 0
    for so in range(a, b + 1):
        if la_so_nguyen_to(so):
            tong += so
    return tong

for line in sys.stdin:
    try:
        a_str, b_str = line.strip().split()
        
        a = int(a_str)
        b = int(b_str)
        
        if a <= 0 or b <= 0 or a > b:
            continue
            
        tong = tinh_tong_so_nguyen_to(a, b)
        print(tong)

    except ValueError:
        continue
    except Exception:
        continue