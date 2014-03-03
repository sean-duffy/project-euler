def sieve(n):
    a = [True] * n
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in xrange(i * i, n, i):
                a[n] = False

for i, p in enumerate(sieve(500000)):
    if i == 10001 - 1:
        print p
        break

print i
