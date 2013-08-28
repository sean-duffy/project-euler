min_limit = 100
max_limit = 999
largest = 0

def is_palindrome(n):
	n = str(n)
	l = len(n)
	if l % 2 == 0:
		if n[:l/2:] == n[:(l/2)-1:-1]:
			return True
	else:
		if n[:((l+1)/2)-1:] == n[:((l+1)/2)-1:-1]:
			return True
	return False

for a in range(min_limit, max_limit+1)[::-1]:
	for b in range(min_limit, max_limit+1)[::-1]:
		if is_palindrome(a*b) and a*b > largest:
			largest = a*b

print largest