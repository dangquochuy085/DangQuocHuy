print("Dang Quoc Huy\nMSV:245752021610171");
import numpy as np

# Định nghĩa kiểu dữ liệu cấu trúc
data_type = [('name', 'S5'), ('class', int), ('height', float)]

# Dữ liệu đầu vào
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]
students = np.array(students_details, dtype=data_type)

print("Original Array:")
print(students)

# Sắp xếp theo trường 'height'
students_sorted = np.sort(students, order='height')

print("\nSort by height:")
print(students_sorted)
