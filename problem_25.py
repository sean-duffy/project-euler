fib_1 = 1;
fib_2 = 1;
n = 0;
i = 2;

while len(str(n)) < 1000:
	n = fib_1 + fib_2
	print n
	fib_1 = fib_2
	fib_2 = n
	i += 1

print
print i