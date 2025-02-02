nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

isPrime = lambda num : num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

prime_nums = filter(isPrime, nums)

print(list(prime_nums))