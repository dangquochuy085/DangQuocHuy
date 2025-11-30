print("Dang Quoc Huy\nMSV:245752021610171");
"""Program make a simple calculator that can add, subtract, multiply and divide using functions"""

# Hàm Cộng
def add(x, y):
    return x + y 

# Hàm Trừ
def subtract(x, y):
    return x - y 

# Hàm Nhân
def multiply(x, y):
    return x * y 

# Hàm Chia
def divide(x, y):
    # Kiểm tra chia cho 0
    if y == 0:
        return "Lỗi: Không thể chia cho 0"
    return x / y

# Menu
print("Chọn phép toán.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Nhận input từ người dùng
choice = input("Chọn (1/2/3/4):")

try:
    num1 = float(input("Nhập số thứ nhất: ")) # Dùng float cho phép chia
    num2 = float(input("Nhập số thứ hai: "))
except ValueError:
    print("Input không hợp lệ. Vui lòng nhập số.")
    # Có thể thoát hoặc gọi lại chương trình ở đây

result = None # Khởi tạo biến kết quả

if choice == '1':
    result = add(num1, num2)
    operator = '+'
elif choice == '2':
    result = subtract(num1, num2)
    operator = '-'
elif choice == '3':
    result = multiply(num1, num2)
    operator = '*'
elif choice == '4':
    result = divide(num1, num2)
    operator = '/'
else:
    print("Input không hợp lệ.")
    
if result is not None:
    print(f"{num1} {operator} {num2} = {result}")
