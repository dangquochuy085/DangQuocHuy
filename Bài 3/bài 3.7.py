print("Dang Quoc Huy\nMSV:245752021610171");
def checkValue(n):
    # Sử dụng toán tử % (modulo) để kiểm tra phần dư khi chia cho 2
    if n % 2 == 0:
        print("Đây là một số chẵn")
    else:
        print("Đây là một số lẻ")

# Ví dụ gọi hàm
checkValue(7) # Output: Đây là một số lẻ
checkValue(10) # Output: Đây là một số chẵn
