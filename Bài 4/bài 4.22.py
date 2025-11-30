print("Dang Quoc Huy\nMSV:245752021610171");
# Đoạn: [1000, 3000]
result = []

for i in range(1000, 3001):
    s = str(i)
    is_all_even = True
    
    # Kiểm tra từng chữ số
    for digit in s:
        # Chuyển chữ số về số nguyên và kiểm tra chẵn
        if int(digit) % 2 != 0: 
            is_all_even = False
            break # Thoát vòng lặp con ngay lập tức
            
    if is_all_even:
        result.append(s)

print(",".join(result))

