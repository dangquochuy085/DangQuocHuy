print("Dang Quoc Huy\nMSV:245752021610171");
# Ví dụ đầu vào: 0100,0011,1010,1001
input_str = input("Nhập chuỗi nhị phân (4 chữ số, cách nhau bởi dấu phẩy): ")
binary_list = input_str.split(',')
result = []

for binary_num in binary_list:
    # 1. Kiểm tra 4 chữ số và chuyển sang thập phân
    if len(binary_num) == 4 and all(c in '01' for c in binary_num):
        decimal_num = int(binary_num, 2)
        
        # 2. Kiểm tra chia hết cho 5
        if decimal_num % 5 == 0:
            # 3. Thêm số nhị phân hợp lệ vào danh sách kết quả (theo yêu cầu)
            result.append(binary_num)
            
# Đầu ra: các số nhị phân thỏa mãn, cách nhau bằng dấu phẩy
print(",".join(result)) 
