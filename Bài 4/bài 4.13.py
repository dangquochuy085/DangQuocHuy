print("Dang Quoc Huy\nMSV:245752021610171");
ds = ['a', 'b', 'c', 'abc'] # Giả định list ban đầu

# Tìm index (vị trí) của phần tử 'abc'
try:
    vi_tri = ds.index('abc')
    print(f"Vị trí của chuỗi 'abc' là: {vi_tri}") # Output: 3
except ValueError:
    print("Không tìm thấy chuỗi 'abc' trong list.")
