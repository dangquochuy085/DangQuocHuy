print("Dang Quoc Huy\nMSV:245752021610171");
import math

# pos[0] là trục y (UP/DOWN), pos[1] là trục x (LEFT/RIGHT)
pos = [0.0, 0.0] 

print("Nhập các lệnh di chuyển (ví dụ: UP 5). Nhập Enter rỗng để kết thúc.")

while True:
    s = input()
    if not s:
        break # Thoát nếu chuỗi input rỗng
        
    # Tách lệnh và bước: Ví dụ "UP 5" -> ["UP", "5"]
    try:
        movement = s.split(" ")
        direction = movement[0].upper() # Lấy hướng, chuyển thành chữ hoa
        steps = int(movement[1])        # Lấy số bước, chuyển thành số nguyên
    except:
        print("Lỗi định dạng lệnh. Vui lòng nhập lại.")
        continue # Bỏ qua lần lặp này

    # Cập nhật vị trí
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps # Trục X giảm
    elif direction == "RIGHT":
        pos[1] += steps # Trục X tăng
    else:
        print(f"Lệnh '{direction}' không hợp lệ. Bỏ qua.")


# Tính khoảng cách từ (pos[1], pos[0]) đến (0, 0)
# Khoảng cách = sqrt(delta_x^2 + delta_y^2)
distance = math.sqrt(pos[1]**2 + pos[0]**2)

# Làm tròn đến số nguyên gần nhất (round()) và in ra
print(f"\nKhoảng cách cuối cùng từ (0,0) là: {distance:.4f}")
print(f"Kết quả làm tròn đến số nguyên gần nhất là: {int(round(distance))}")
