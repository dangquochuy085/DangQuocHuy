print("Dang Quoc Huy\nMSV:245752021610171");
# Giả sử giao dịch được nhập theo dòng (hoặc cách nhau bởi dấu phẩy và dấu cách)
print("Nhập nhật ký giao dịch (ví dụ: D 100, W 50). Nhập Enter rỗng để kết thúc.")

balance = 0 # Khởi tạo số dư tài khoản

while True:
    transaction = input()
    if not transaction:
        break # Thoát nếu input rỗng
        
    try:
        # Tách lệnh (D/W) và số tiền
        parts = transaction.split()
        operation = parts[0].upper()
        amount = int(parts[1])
        
        if operation == 'D':
            balance += amount
        elif operation == 'W':
            balance -= amount
        else:
            print(f"Lệnh '{operation}' không hợp lệ. Bỏ qua.")
            
    except (IndexError, ValueError):
        print("Lỗi định dạng giao dịch. Vui lòng nhập lại (ví dụ: D 100).")
        continue

print(f"Số tiền thực trong tài khoản là: {balance}")
