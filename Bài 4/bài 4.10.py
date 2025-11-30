print("Dang Quoc Huy\nMSV:245752021610171");
ds = input('Nhập chuỗi: ').split() 
# Ví dụ ds = ['mot', 'hai', 'ba', 'bon', 'nam']

# Slicing: ds[start:end:step]
# [1: -1] lấy từ index 1 đến index trước index -1 (trước phần tử cuối)
x = ds[1:-1] 

print(f"List ban đầu: {ds}")
print(f"List sau khi cắt: {x}") 

# In từng phần tử của list đã cắt
# for c in x:
#     print(c)
