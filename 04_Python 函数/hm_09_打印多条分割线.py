def print_line(char, times):
    """title: 打印单行分割线

    :param char: 分隔字符
    :param times: 重复次数
    """
    print(char * times)


def print_lines(num, char, times):
    """title: 打印多行分割线

    :param num: 打印次数
    :param char: 打印分隔线使用的分隔字符
    :param times: 分隔线字符重复的次数
    """
    row = 0
    while row <= num:

        print_line(char, times)

        row += 1


print_lines(4, "-", 34)
