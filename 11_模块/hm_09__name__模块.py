# 全局变量、函数、类，注意：直接执行的代码不是向外界提供的工具

def say_hello():
    print("您好你好， 我是say hello")


# 如果直接执行模块，__main__
if __name__ == '__main__':

    print(__name__, '123')

    # 文件被导入时，能够直接执行的代码不需要被执行！
    print("小明开发的")
    say_hello()