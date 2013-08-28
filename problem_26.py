from decimal import *

getcontext().prec = 10000

def recursion_length(n):
	f = str(1/Decimal(n))[2::]
	for cycle_length in range(1, 10000):
		part_one = f[0:0+cycle_length:]
		part_two = f[cycle_length:cycle_length*2:]
		part_three = f[cycle_length*2:cycle_length*3:]
		if part_one == part_two and part_two == part_three:
			return cycle_length
	return 0

longest_cycle = 0

for i in range(1, 1000):
	if recursion_length(i) > longest_cycle:
		i_longest = i
		longest_cycle = recursion_length(i)

print
print i_longest