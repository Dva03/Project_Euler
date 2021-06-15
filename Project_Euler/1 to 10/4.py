first_num = 0
second_num = 0
max_num = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        num = i * j
        first_digits = str(num // 1000)[::-1]
        last_digits = str(num % 1000)
        if first_digits == last_digits and max_num < num :
            first_num = i
            second_num = j
            max_num = num
print(first_num, second_num, first_num*second_num) # 913 * 993 = 906609
