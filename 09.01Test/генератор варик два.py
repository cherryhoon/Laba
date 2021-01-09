def divisors(n):
    # получить множители и их количество
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            factors[i] = factors.get(i, 0) + 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = factors.get(nn, 0) + 1
 
    primes = list(factors.keys())
 
    # сгенерировать множители из подмножества 
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime
 
    for factor in generate(0):
        if factor % 2 != 0:
            yield factor
 
            
            
for e in divisors(9):
    print(e)