limit = 28124

def divisor_sum(n):
	d_sum = 0
	for d in range(1, n):
		if n % d == 0:
			d_sum += d
	return d_sum

def is_abundant(n):
	if divisor_sum(n) > n:
		return True
	else:
		return False

abundant_numbers = []

for i in range(12, limit+1):
	print str(round((float(i)/limit) * 100)) + '%'
	if is_abundant(i):
		abundant_numbers.append(i)

def abundant_summable(n):
	a = 0
	while abundant_numbers[a] < n:
		if abundant_numbers.count(n - abundant_numbers[a]) != 0:
			return True
		a += 1
	return False

total = 0

for i in range(24, limit+1):
	print str(round((float(i)/limit) * 100)) + '%'
	if not abundant_summable(i):
		total += i

print total