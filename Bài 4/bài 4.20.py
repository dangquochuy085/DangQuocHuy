print("Dang Quoc Huy\nMSV:245752021610171");
def pascal_triangle(n):
    """Tạo n dòng đầu tiên của tam giác Pascal."""
    result = []
    
    for i in range(n):
        row = [1] * (i + 1) # Mỗi dòng bắt đầu và kết thúc bằng 1
        
        # Nếu dòng > 2, tính các giá trị ở giữa
        if i >= 2:
            # Giá trị của một ô = Tổng hai ô phía trên nó ở dòng trước
            prev_row = result[i-1]
            for j in range(1, i):
                row[j] = prev_row[j-1] + prev_row[j]
        
        result.append(row)
        
    # In ra tam giác Pascal
    for row in result:
        # Căn giữa và in các số, cách nhau bởi khoảng trắng
        print(' '.join(map(str, row)).center(n * 4))

n = int(input("Nhập số dòng n: "))
pascal_triangle(n)
