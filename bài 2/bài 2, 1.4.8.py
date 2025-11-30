print("Dang Quoc Huy\nMSV:245752021610171");
a, b = 1, 2 # Khởi tạo 2 số đầu tiên của dãy
total = 0 # Biến tích lũy tổng các số chẵn
limit = 4000000 

print("Dãy Fibonacci:", end=" ")

# Vòng lặp dừng khi số Fibonacci hiện tại (a) vượt quá giới hạn
while a < limit:
    # 1. Kiểm tra số chẵn và cộng vào total
    if a % 2 == 0:
        total += a
    
    # 2. In số hiện tại
    print(a, end=", ")
    
    # 3. Tính số tiếp theo trong dãy (Fibonacci sequence update)
    a, b = b, a + b

print(f"\nTổng các số chẵn trong dãy (nhỏ hơn {limit}) là: {total}")
# Lưu ý: Đoạn code mẫu trong ảnh dùng 4000000-1 và có in "n sum of prime numbers term..."
# đã được sửa lại để đúng với yêu cầu tính TỔNG SỐ CHẴN và giới hạn < 4.000.000.
