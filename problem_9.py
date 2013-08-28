def triplet(n):
	for a in range(n):
		for b in range(n):
			for c in range(n):
				if (a**2 + b**2)**0.5 == c:
					if a+b+c == 1000:			
						return a*b*c

print triplet(500)