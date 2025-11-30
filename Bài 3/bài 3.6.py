print("Dang Quoc Huy\nMSV:245752021610171");
def get_sum(*num):
    # num là một tuple chứa tất cả các đối số được truyền vào (1, 2, 3, 4, 5)
    tmp = 0 
    
    # Duyệt qua các tham số (các phần tử trong tuple num)
    for i in num:
        tmp += i # Cộng dồn tổng
        
    return tmp

# Gọi hàm với 5 đối số
result = get_sum(1, 2, 3, 4, 5) 
print(result) # Output: 15

# Gọi hàm với số lượng đối số khác
result_2 = get_sum(10, 20)
print(result_2) # Output: 30
