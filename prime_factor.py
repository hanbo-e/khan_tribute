# naive prime-factorization algorithm
FIRST_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)

def prime_factors(my_integer: int) -> int:
	temp = my_integer
	for my_prime in FIRST_PRIMES:
		while (temp % my_prime == 0):
			print(my_prime)
			temp = temp / my_prime

if __name__ == "__main__":
	prime_factors(24)

