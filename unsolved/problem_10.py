def sieve(n):
    a = [True] * n
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in xrange(i * i, n, i):
                a[n] = False

primes = []

for p in sieve(3000000):
    if p < 2000000:
        primes.append(p)

print sum(primes)
