print("Dang Quoc Huy\nMSV:245752021610171");
# Nhập chuỗi: Ví dụ: apple,zebra,banana,orange
input_str = input("Nhập các từ cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành list các từ
words = input_str.split(',')

# Loại bỏ khoảng trắng thừa ở hai đầu mỗi từ
cleaned_words = [word.strip() for word in words]

# Sắp xếp list theo thứ tự từ điển (Alphabetical)
cleaned_words.sort()

print("Các từ theo thứ tự từ điển:")
for word in cleaned_words:
    print(word)
