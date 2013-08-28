sum_natural = 0
sum_squares = 0

for i in range(1, 101):
	sum_natural += i
	sum_squares += i**2

print sum_natural**2 - sum_squares