def divisor_sum(n):
	d_sum = 0
	for d in range(1, n):
		if n % d == 0:
			d_sum += d
	return d_sum

def is_amicable(n1):
	n2 = divisor_sum(n1)
	if divisor_sum(n2) == n1 and n1 != n2:
		return True
	else:
		return False

total = 0

for i in range(10000):
	if is_amicable(i):
		total += i

print total