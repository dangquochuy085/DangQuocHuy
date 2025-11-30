print("Dang Quoc Huy\nMSV:245752021610171");
import math

def Tinh(R):
    # Kiểm tra R có hợp lệ (R phải là số dương)
    if R <= 0:
        return "Bán kính phải là số dương", "Bán kính phải là số dương"
        
    # Tính Chu vi
    chu_vi = 2 * math.pi * R
    
    # Tính Diện tích
    dien_tich = math.pi * (R ** 2)
    
    # Trả về cả hai giá trị
    return chu_vi, dien_tich 

# Nhập bán kính
try:
    R = float(input("Nhập bán kính R: "))
    
    # Gọi hàm và nhận hai giá trị trả về
    C, A = Tinh(R) 
    
    print(f"Bán kính R = {R}")
    print(f"Chu vi hình tròn (C) = {C:.4f}")
    print(f"Diện tích hình tròn (A) = {A:.4f}")
    
except ValueError:
    print("Vui lòng nhập giá trị số cho bán kính.")
