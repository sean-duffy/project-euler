count = 0

for i in range(2**3 + 1, 2**4 - 1):
	print bin(i)[2::]
	count += 1

print
print count