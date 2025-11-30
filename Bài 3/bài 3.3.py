print("Dang Quoc Huy\nMSV:245752021610171");
a = "Hello!" # Biến toàn cục (Global Variable)

def say_hello():
    # Hàm này không sử dụng biến a
    pass

print(a) # Output: Hello!
say_hello() 
print(a) # Output: Hello!
