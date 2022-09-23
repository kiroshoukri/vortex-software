def power_number(base_num, pow):
    flag = 1
    for i in range (pow):
        flag = flag * base_num
    return flag

print(power_number(3,3))

