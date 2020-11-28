odds = {1,3,5,7}
evens = {2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)
i2 = odds.intersection(primes)
print(i2)