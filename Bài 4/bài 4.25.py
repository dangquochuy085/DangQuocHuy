print("Dang Quoc Huy\nMSV:245752021610171");
# Nhập chuỗi và tách thành list các chuỗi số
input_str = input("Nhập các số cách nhau bởi dấu phẩy: ")
str_list = input_str.split(',')
odd_list = []

for item in str_list:
    # 1. Chuyển chuỗi thành số nguyên
    try:
        num = int(item.strip())
        
        # 2. Kiểm tra số lẻ (phần dư khi chia 2 khác 0)
        if num % 2 != 0:
            odd_list.append(str(num)) # Chuyển lại thành chuỗi để join
            
    except ValueError:
        # Bỏ qua nếu không phải là số hợp lệ
        pass 

print(",".join(odd_list))
