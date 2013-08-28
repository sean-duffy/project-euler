f = 1
divisor_count = 0

while divisor_count < 501:
	n = sum([j for j in range(f)])
	divisor_count = 0
	for i in range(1, n+1):
		if n % i == 0:
			divisor_count += 1
	print n, divisor_count
	f += 1

print n