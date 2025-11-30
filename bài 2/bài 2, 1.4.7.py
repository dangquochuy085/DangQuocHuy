print("Dang Quoc Huy\nMSV:245752021610171");
n=int(input("Nhập vào một số:"))
d=dict() # Khởi tạo dictionary rỗng
for i in range(1,n+1): # Lặp từ 1 đến n (bao gồm n)
    d[i]=i*i # Gán key là i và value là i*i
print(d)
