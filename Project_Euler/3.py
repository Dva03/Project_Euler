# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
full_num = 600851475143
num = int(pow(full_num, 0.5))
max_factor = 1
d = 2
while d < num:
    if full_num % d == 0:
        max_factor = d
        full_num //= d
    else:
        d += 1
if full_num > 1:
    max_factor = full_num

print(max_factor) # max_factor = 6857