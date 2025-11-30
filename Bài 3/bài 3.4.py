print("Dang Quoc Huy\nMSV:245752021610171");
# a là biến TOÀN CỤC (Global)
a = "Hello Guy!" 
print(a) # Output: Hello Guy!

def say():
    # a ở đây là biến CỤC BỘ (Local) mới, độc lập với biến toàn cục
    a = "Vinh University" 
    print(a)

say() # Gọi hàm, in ra biến cục bộ a: Output: Vinh University

# Lệnh print này in ra biến TOÀN CỤC a
print(a) # Output: Hello Guy!
