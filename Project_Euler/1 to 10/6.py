#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
result = 0
for i in range(1, 101):
    for j in range(i + 1, 101):
        result += i*j
result *= 2
print(result) # result = 25164150