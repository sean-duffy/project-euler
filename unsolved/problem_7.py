def prime(n):
	prime = True
	for i in range(2, n):
		if n % i == 0:
			prime = False
	if prime:
		return True
	else:
		return False

primes = []
i = 3

while len(primes) < 10002:
	if prime(i):
		primes.append(i)
		print len(primes), '=', i
	i += 2