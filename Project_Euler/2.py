# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
past_num = 1
num = 2
result_sum = 2
while num < 4000000:
    past_num, num = num, past_num + num
    if num % 2 == 0:
        result_sum += num
print(result_sum) #result_sum = 4613732