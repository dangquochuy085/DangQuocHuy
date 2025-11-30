print("Dang Quoc Huy\nMSV:245752021610171");
sentence = input("Nhập câu: ")
upper_count = 0
lower_count = 0

for char in sentence:
    if char.isupper(): # Kiểm tra có phải là chữ hoa
        upper_count += 1
    elif char.islower(): # Kiểm tra có phải là chữ thường
        lower_count += 1

print(f"Chữ hoa: {upper_count}")
print(f"Chữ thường: {lower_count}")
