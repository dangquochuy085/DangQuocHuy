print("Dang Quoc Huy\nMSV:245752021610171");
str_input = input("Enter a String:")
dict_count = {} 

# Phương pháp 1: Duyệt qua từng ký tự
for char in str_input:
    # Nếu ký tự đã có trong dictionary, tăng giá trị lên 1
    if char in dict_count:
        dict_count[char] += 1
    # Nếu chưa có, gán giá trị khởi tạo là 1
    else:
        dict_count[char] = 1
        
print(dict_count)

# Hoặc Phương pháp 2: Sử dụng phương thức count() (ít hiệu quả hơn cho chuỗi dài)
# str_input = input("Enter a String:")
# dict_count_2 = {}
# for char in set(str_input): # Chỉ lặp qua các ký tự duy nhất
#     dict_count_2[char] = str_input.count(char)
# print(dict_count_2)
