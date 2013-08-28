num = 600851475143
factors = []

for i in range(1, 10000000):
	if num % i == 0:
		factors.append(i)
		print i

p = factors[0]

while n < 