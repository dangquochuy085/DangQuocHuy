print("Dang Quoc Huy\nMSV:245752021610171");
j=[]
for i in range(2000, 3201):
    # Kiểm tra: chia hết cho 7 (i % 7 == 0) VÀ không chia hết cho 5 (i % 5 != 0)
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i)) # Chuyển số thành chuỗi để dùng join
print(','.join(j))
