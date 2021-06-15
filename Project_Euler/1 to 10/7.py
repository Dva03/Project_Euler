#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
i = 0
dividers_list = [2]
while i != 10001:
    i += 1
    next_num = dividers_list[i - 1] + 1
    key = True
    while key:
        for i_divider in dividers_list:
            if next_num % i_divider == 0:
                key = False
                break

        if not key:
            key = True
        else:
            dividers_list.append(next_num)
            break
        next_num += 1
print(dividers_list[10000])  # 104743
