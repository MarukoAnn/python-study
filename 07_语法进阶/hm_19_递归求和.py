# 定义一个函数 sum_numbers
# 能够接受一个num的整数参数
# 计算 1 + 2 + ... num的结果

def sum_numbers(num):
    # 出口
    if num == 1:
        return 1
    # 数字累加 num + (1...num -1)
    # 假设sum_numbers 能够正确处理 1.. num -1
    temp = sum_numbers(num -1)
    # 两个数字相加
    return num + temp


result = sum_numbers(100)

print(result)
