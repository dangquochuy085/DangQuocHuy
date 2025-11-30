print("Dang Quoc Huy\nMSV:245752021610171");
# Ví dụ: 0100,0011,1010,1001
input_str = input("Nhập các số nhị phân cách nhau bởi dấu phẩy: ")
binary_list = input_str.split(',')
result = []

for binary_num in binary_list:
    # 1. Chuyển số nhị phân sang số thập phân
    try:
        decimal_num = int(binary_num, 2) # int(string, base)
        
        # 2. Kiểm tra xem số thập phân có chia hết cho 5 không
        if decimal_num % 5 == 0:
            # 3. Thêm số thập phân hợp lệ vào danh sách kết quả
            result.append(str(decimal_num))
            
    except ValueError:
        # Bỏ qua nếu chuỗi không phải là số nhị phân hợp lệ
        pass 

# In ra kết quả, cách nhau bởi dấu phẩy
print(",".join(result))


