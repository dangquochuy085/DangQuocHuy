print("Dang Quoc Huy\nMSV:245752021610171");
a="hi i am python programmer"
# Sử dụng split() để tách chuỗi thành danh sách (mặc định tách bằng khoảng trắng)
b=a.split()
print("Kết quả Split:", b) # Output: ['hi', 'i', 'am', 'python', 'programmer']

# Sử dụng join() để nối các phần tử trong danh sách lại thành chuỗi, 
# sử dụng một chuỗi rỗng làm dấu phân cách
c=" ".join(b)
print("Kết quả Join:", c) # Output: hi i am python programmer

# Thử với dấu phân cách khác, ví dụ: "_"
d="_".join(b)
print("Kết quả Join (dùng '_'):", d) # Output: hi_i_am_python_programmer
