print("Dang Quoc Huy\nMSV:245752021610171");
import math
# Nhập tọa độ điểm 1
x1=int(input("Enter x1--->"))
y1=int(input("Enter y1--->"))
# Nhập tọa độ điểm 2
x2=int(input("Enter x2--->"))
y2=int(input("Enter y2--->"))

# Tính bình phương hiệu các tọa độ
d1 = (x2 - x1) * (x2 - x1)
d2 = (y2 - y1) * (y2 - y1)
# Tổng bình phương hiệu các tọa độ
sum_of_squares = d1 + d2 
# Tính căn bậc hai
res = math.sqrt(sum_of_squares) 

print("Distance between two points:",res)
