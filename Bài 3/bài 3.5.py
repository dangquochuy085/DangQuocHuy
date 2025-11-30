print("Dang Quoc Huy\nMSV:245752021610171");
# a là biến TOÀN CỤC
a = "Hello Guy!" 
print(a) # Output: Hello Guy!

def say():
    # Khai báo sử dụng biến toàn cục a
    global a 
    # Bây giờ, phép gán này thay đổi biến toàn cục a
    a = "Vinh University" 
    print(a)

say() # Gọi hàm, in ra a đã được thay đổi: Output: Vinh University

# Lệnh print này in ra biến TOÀC CỤC a đã BỊ THAY ĐỔI
print(a) # Output: Vinh University
