num = 10


def demo():
    # 希望修全局变量的值
    # 在Python 中，是不允许直接修改全局变量的值
    # 如果使用赋值语句，会在函数内部，定义一个局部变量
    num = 99

    print("demo ===> %d" % num)


def demo2():

    print("demo2 ===> %d" % num)


demo()
demo2()

