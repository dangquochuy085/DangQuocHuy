print("Dang Quoc Huy\nMSV:245752021610171");
import turtle
import random

# Thiết lập cửa sổ
window = turtle.Screen()
window.bgcolor("white") # Có thể đặt màu nền khác

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0) # Tăng tốc độ vẽ lên tối đa

for i in range(10):
    # Chọn ngẫu nhiên một màu từ danh sách
    color = random.choice(colors) 
    painter.pencolor(color)
    
    # Vẽ hình tròn bán kính 100
    painter.circle(100) 
    
    # Quay rùa sang phải 30 độ
    painter.right(30)
    
    # Di chuyển rùa sang trái 60 độ (quay rùa, không di chuyển vị trí)
    painter.left(60)
    
    # Dòng này trong ảnh gốc là setposition(0, 0), nhưng có thể bỏ qua 
    # nếu muốn xem hiệu ứng xoay. Giữ nguyên theo ảnh:
    painter.setposition(0, 0) # Đặt lại vị trí về tâm (0, 0)
    
# Thêm dòng này để cửa sổ không đóng ngay lập tức
window.mainloop()
