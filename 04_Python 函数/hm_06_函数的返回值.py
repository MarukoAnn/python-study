def sum_2_num(num1, num2):
    """
    title: 求和函数 \n
    :param num1: 传递参数一
    :param num2: 传递参数二
    :return: 返回两个参数的和
    """
    # 可以使用返回值, 告诉调用函数一方计算的结果
    return num1 + num2
    # 注意：return 就表示返回，下方代码不会继续被执行
    # rum = 1000

# 可以使用变量，来接收函数执行的返回结果
result = sum_2_num(13, 7)

print(result)