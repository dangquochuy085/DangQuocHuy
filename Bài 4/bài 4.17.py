print("Dang Quoc Huy\nMSV:245752021610171");
def sum_of_divisors(num):
    """Tính tổng các ước số thực sự (Proper divisors) của num."""
    total = 1 # 1 luôn là ước
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            total += i
            # Thêm ước số đối ngẫu (trừ khi nó là căn bậc hai)
            if i != num // i:
                total += num // i
    return total

def is_abundant(n):
    """Kiểm tra xem n có phải là số thừa (Abundant) không."""
    if n <= 1:
        return False
    return sum_of_divisors(n) > n # Tổng các ước thực sự > n

n = int(input("Nhập số nguyên n: "))
result = []

for i in range(1, n):
    if is_abundant(i):
        result.append(str(i))

print(f"Các số thừa nhỏ hơn {n}: {', '.join(result)}")
