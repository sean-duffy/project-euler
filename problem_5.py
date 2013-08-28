i = 100000
found = False

while not found:
	found = True
	for n in range(1, 21):
		if i % n != 0:
			found = False
			break
	i += 20

print i - 20