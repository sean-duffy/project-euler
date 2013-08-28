fib = [1, 2]
i = 2
n = 0

while n < 4000000:
	n = fib[i - 1] + fib[i - 2]
	fib.append(n)
	i += 1

print sum(filter(lambda x: x % 2 == 0, fib))