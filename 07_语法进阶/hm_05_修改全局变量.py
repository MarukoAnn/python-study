num = 10


def demo():
    # 希望修全局变量的值
    # global 关键字会告诉解释器后面的变量是一个全局变量
    # 在使用赋值语句时，就不会创建局部变量
    global num

    num = 99

    print("demo ===> %d" % num)


def demo2():

    print("demo2 ===> %d" % num)


demo()
demo2()

