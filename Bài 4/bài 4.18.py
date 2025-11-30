print("Dang Quoc Huy\nMSV:245752021610171");
n = int(input("Nhập số nguyên n: "))
fib_list = []

# Khởi tạo 2 số đầu tiên
a, b = 0, 1 

# Thêm số 0 và 1 nếu chúng nhỏ hơn n
if a < n:
    fib_list.append(a)
if b < n:
    fib_list.append(b)
    
# Tính các số tiếp theo
while True:
    next_fib = a + b
    if next_fib >= n:
        break
    
    fib_list.append(next_fib)
    # Cập nhật a và b
    a, b = b, next_fib

# Loại bỏ số 0 nếu n < 2 (vì list sẽ có 0 và 1) và đảm bảo không trùng lặp
final_fib_list = sorted(list(set(fib_list)))

print(f"Các số Fibonacci nhỏ hơn {n}: {final_fib_list}")
