print("Dang Quoc Huy\nMSV:245752021610171");
sentence = input("Nhập câu: ")
letters = 0
digits = 0

for char in sentence:
    if char.isalpha(): # Kiểm tra có phải là chữ cái (A-Z, a-z)
        letters += 1
    elif char.isdigit(): # Kiểm tra có phải là chữ số (0-9)
        digits += 1
        
print(f"Số chữ cái là: {letters}")
print(f"Số chữ số là: {digits}")
