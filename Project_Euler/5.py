# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def euclid_algorithm(n,m):
    while n != m:
        if n > m:
            n = n - m
        else:
            m = m - n
    return n
def lowest_total(n,m):
    nod = euclid_algorithm(n,m)
    return n * m / nod
i_nok = 1
for i in range(1, 21):
    i_nok = lowest_total(i, i_nok)
print(i_nok)