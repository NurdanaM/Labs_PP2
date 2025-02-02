def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(nums):
    return [n for n in nums if is_prime(n)]

nums = [2, 4, 9, 5, 3, 10, 17, 19, 18]
prime_nums = filter_prime(nums)
print("Prime numbers:", prime_nums)
