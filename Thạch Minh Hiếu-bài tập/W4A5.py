def tim_y_nghia_cuoc_song():    
    while True:
        try:
            n = int(input("Vui lòng nhập số nguyên dương n (số lượng phần tử của dãy): "))
            if n > 0:
                break
            else:
                print("Lỗi: n phải là số nguyên dương. Vui lòng nhập lại.")
        except ValueError:
            print("Lỗi: Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
            
    print(f"\nBây giờ, vui lòng nhập {n} số nguyên, cách nhau bởi dấu cách:")
    
    while True:
        try:
            dau_vao_chuoi = input().split()   

            if len(dau_vao_chuoi) != n:
                print(f"Lỗi: Bạn phải nhập đúng {n} số. Vui lòng nhập lại.")
                continue

            day_so = [int(so) for so in dau_vao_chuoi]
            break

        except ValueError:
            print("Lỗi: Một hoặc nhiều phần tử không phải là số nguyên. Vui lòng nhập lại.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}. Vui lòng thử lại.")
            
    if 42 in day_so:
        print("I've found the meaning of life!")
    else:
        print("It's a joke!")

tim_y_nghia_cuoc_song()