print("Dang Quoc Huy\nMSV:245752021610171");
import numpy as np

student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.])

# Sử dụng np.lexsort để sắp xếp ID theo Height (Height là mảng cuối cùng trong tuple)
# Mảng cần sắp xếp ID là mảng thứ 2. Mảng tiêu chí sắp xếp là Height (mảng thứ 1)
indices = np.lexsort((student_height,)) 

print("Chỉ số:", indices) # Chỉ số: [4 0 5 3 6 1 2]

# Áp dụng chỉ số đã sắp xếp lên cả hai mảng
sorted_ids = student_id[indices]
sorted_heights = student_height[indices]

print("\nDữ liệu sắp xếp:")
for sid, sh in zip(sorted_ids, sorted_heights):
    print(f"{sid}\t{sh}")
