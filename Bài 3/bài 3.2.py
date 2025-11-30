    
def sum_with_return(a, b):
    return a + b # Trả về giá trị a + b

# Gọi hàm và gán giá trị trả về cho biến c
c = sum_with_return(4, 5) 
print("Tổng của 4 và 5 = " + str(c)) # Output: Tổng của 4 và 5 = 9

# Có thể gọi trực tiếp hàm trong lệnh print
print("Tổng của 3 và 7 = " + str(sum_with_return(3, 7))) # Output: Tổng của 3 và 7 = 10
