print("Dang Quoc Huy\nMSV:245752021610171");
def sieve_of_eratosthenes(limit):
    """Sử dụng Sàng Eratosthenes để tìm các số nguyên tố."""
    # Khởi tạo một list boolean (True = là số nguyên tố)
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False # 0 và 1 không phải là số nguyên tố
    
    # Bắt đầu từ 2
    p = 2
    while (p * p <= limit):
        # Nếu is_prime[p] không bị thay đổi, thì nó là một số nguyên tố
        if is_prime[p]:
            # Đánh dấu tất cả bội số của p là không phải nguyên tố
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
        
    # Xây dựng list các số nguyên tố
    primes = [i for i, is_p in enumerate(is_prime) if is_p]
    return tuple(primes) # Trả về dưới dạng Tuple

limit = 1000000
P = sieve_of_eratosthenes(limit)

print(f"Đã tạo Tuple P gồm {len(P)} số nguyên tố nhỏ hơn {limit}.")
# print(f"Một số số nguyên tố đầu tiên: {P[:10]}")
# print(f"Một số số nguyên tố cuối cùng: {P[-10:]}")
