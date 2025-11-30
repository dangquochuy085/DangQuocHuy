print("Dang Quoc Huy\nMSV:245752021610171")
import re # Cần thư viện re (Regular Expression)

# Nhập chuỗi mật khẩu, ví dụ: "AbD1234@1,a F1#,2w3E*,2We3345"
password_input = input("Nhập mật khẩu (cách nhau bằng dấu phẩy):")

# Tách chuỗi thành danh sách các mật khẩu
items = password_input.split(',')
value = [] # Danh sách lưu các mật khẩu hợp lệ

# Định nghĩa các biểu thức chính quy (Regular Expressions)
# SỬ DỤNG 'r' (Raw String) để tránh lỗi/cảnh báo 'invalid escape sequence'
regex_lower = re.compile('[a-z]')
regex_upper = re.compile('[A-Z]')
regex_digit = re.compile('[0-9]')
regex_special = re.compile('[$#@]')
regex_whitespace = re.compile(r'\s') # <<< ĐÃ THÊM 'r' Ở ĐÂY

for p in items:
    # 1. Kiểm tra độ dài
    if not (6 <= len(p) <= 12):
        continue # Bỏ qua mật khẩu này
    
    # 2. Kiểm tra các tiêu chí khác (Tất cả đều phải tìm thấy, KHOẢNG TRẮNG thì không được tìm thấy)
    
    # re.search() trả về None nếu không tìm thấy pattern
    if not regex_lower.search(p):
        continue
    if not regex_digit.search(p):
        continue
    if not regex_upper.search(p):
        continue
    if not regex_special.search(p):
        continue
    if regex_whitespace.search(p): # Nếu CÓ khoảng trắng thì BỎ QUA
        continue
    
    # Nếu vượt qua tất cả các kiểm tra
    value.append(p)

# In các mật khẩu hợp lệ, cách nhau bằng dấu phẩy
print(",".join(value))
