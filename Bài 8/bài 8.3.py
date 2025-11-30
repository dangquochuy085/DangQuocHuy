print("Dang Quoc Huy\nMSV:245752021610171");
import turtle

window = turtle.Screen()
window.bgcolor("white")
painter = turtle.Turtle()
painter.pensize(2)
painter.speed(0) # Tăng tốc độ vẽ

colors = ["red", "green", "blue", "orange", "purple", "pink"]

# Lặp 36 lần để tạo hình dáng hoa
for i in range(36):
    # Đổi màu sau mỗi 6 lần lặp (hoặc dùng i % len(colors) để đổi màu theo danh sách)
    painter.pencolor(colors[i % len(colors)]) 
    
    # Vẽ hình tròn bán kính 100
    painter.circle(100) 
    
    # Xoay rùa 10 độ. 36 lần * 10 độ = 360 độ (một vòng tròn đầy đủ)
    painter.left(10) 

window.mainloop()
