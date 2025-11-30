print("Dang Quoc Huy\nMSV:245752021610171");
print("Số  | Nghịch đảo")
print("----|-------------")
i=1;
# Giả định a=1, b=10 -> khoảng (1, 10) là các số 2, 3, ..., 9
for j in range(2,10): 
    # Tính nghịch đảo dưới dạng thập phân
    inverse_value = 1/j 
    # In kết quả. Dùng f-string để định dạng
    print(f"{j:^4} | {inverse_value:.8f}")
