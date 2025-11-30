print("Dang Quoc Huy\nMSV:245752021610171");
def benefit(t, n, k):
    # Chuyển lãi suất t (%) thành số thập phân (t / 100)
    monthly_rate = t / 100 
    
    # Tính tổng tiền theo công thức lãi suất kép
    # Tổng tiền = Vốn ban đầu * (1 + lãi suất/tháng)^số tháng
    total_amount = n * ((1 + monthly_rate) ** k)
    
    return total_amount

# Nhập các tham số
try:
    t_percent = float(input("Nhập lãi suất t (%/tháng): "))
    n_capital = float(input("Nhập vốn ban đầu n: "))
    k_months = int(input("Nhập số tháng k: "))
    
    # Gọi hàm
    final_amount = benefit(t_percent, n_capital, k_months)
    
    print(f"\nThông tin:")
    print(f"Lãi suất hàng tháng: {t_percent}%")
    print(f"Vốn ban đầu: {n_capital:,.2f} VNĐ")
    print(f"Thời gian: {k_months} tháng")
    print(f"Tổng số tiền nhận được sau {k_months} tháng: {final_amount:,.2f} VNĐ")
    
except ValueError:
    print("Input không hợp lệ. Vui lòng nhập số cho lãi suất và vốn, và số nguyên cho số tháng.")
