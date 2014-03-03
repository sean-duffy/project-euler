n = 600851475143

def sieve(n):
    a = [True] * n
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in xrange(i * i, n, i):
                a[n] = False

prime_factors = []

for p in sieve(int(n ** 0.5)):
    if n % p == 0:
        prime_factors.append(p)

print prime_factors[-1]
