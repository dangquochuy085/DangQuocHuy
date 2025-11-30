print("Dang Quoc Huy\nMSV:245752021610171");
ds = ['a', 'b', 'c', '123'] # Giả định list ban đầu
print(f"List ban đầu: {ds}")

# Xóa phần tử có giá trị '123'
try:
    ds.remove('123')
except ValueError:
    print("Phần tử '123' không có trong list.")

print(f"List sau khi xóa: {ds}")
# Output: ['a', 'b', 'c']

# In từng phần tử
# for ch in ds:
#     print(ch)
