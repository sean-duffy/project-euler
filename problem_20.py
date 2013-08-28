total = 0
factorial = 1

for i in range(2, 101):
	factorial *= i

for c in str(factorial):
	total += int(c)

print total