print("Dang Quoc Huy\nMSV:245752021610171");
import math

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    # Trường hợp đặc biệt: Phương trình bậc nhất bx + c = 0
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print(f"Đây là phương trình bậc nhất. Nghiệm x = {x:.4f}")
else:
    # Tính Delta
    delta = b**2 - 4*a*c 
    
    if delta < 0:
        # Nếu delta âm, có 2 nghiệm phức
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-delta) / (2*a)
        print("Phương trình có hai nghiệm phức:")
        print(f"x1 = {real_part:.4f} + {imaginary_part:.4f}i")
        print(f"x2 = {real_part:.4f} - {imaginary_part:.4f}i")
    elif delta == 0:
        # Nếu delta bằng 0, có nghiệm kép
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép x1 = x2 = {x:.4f}")
    else:
        # Nếu delta dương, có 2 nghiệm thực phân biệt
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có hai nghiệm phân biệt:")
        print(f"x1 = {x1:.4f}")
        print(f"x2 = {x2:.4f}")
