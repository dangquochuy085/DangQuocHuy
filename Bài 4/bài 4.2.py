print("Dang Quoc Huy\nMSV:245752021610171");
S = input('Nhập chuỗi: ')
for ch in S:
    # Nếu không phải là khoảng trắng/tab, thì in ra
    if not ch.isspace():
        print(ch)
