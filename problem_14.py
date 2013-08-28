max_count = 0

def collatz(n):
	if n == 0:
		return 1

	if n % 2 == 0:
		return n/2
	else:
		return (3*n) + 1

for i in range(1, 1000000):
	n = i
	count = 0
	while n > 1:
		n = collatz(n)
		count += 1

	if count > max_count:
		max_count = count
		solution = i

print solution