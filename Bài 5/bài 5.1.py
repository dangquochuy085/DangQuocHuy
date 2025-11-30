# Script sử dụng module
import mymath
import mymath as mt  # Có thể dùng alias để gọi ngắn gọn hơn

values = [2, 4, 6, 8, 10]

print('Squares:')
for v in values:
    print(mymath.square(v))

print('Cubes:')
for v in values:
    print(mt.cube(v))

print('Average: ' + str(mymath.average(values)))

# Ví dụ gọi hàm từ alias
print(f"mt.square(2) = {mt.square(2)}")
print(f"mt.square(3) = {mt.square(3)}")
