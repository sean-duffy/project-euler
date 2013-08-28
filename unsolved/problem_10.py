prime_sum = 0

def prime(n):

	if str(n)[-1] == '3' or str(n)[-1] == '5' or str(n)[-1] == '9':
		return False
	prime = True
	for i in range(2, n):
		if n % i == 0:
			prime = False
	if prime:
		return True
	else:
		return False

for i in range(3, 2000000)[::2]:
	if prime(i):
		print i
		prime_sum += i

print
print prime_sum