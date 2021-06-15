# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
def eratosthen(n):
    masieve = list(range(n))
    masieve[1] = 0
    for i in masieve[2:]:
            for j in range(i + i, len(masieve), i):
                masieve[j] = 0
    return masieve

print(sum(eratosthen(2000000)))