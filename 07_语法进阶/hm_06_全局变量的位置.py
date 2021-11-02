# 注意： 在开发时，应该把模块中的所有全局变量
# 定义在所有的函数上方，就可以保证每个函数都可以访问到变量
gl_num = 10
# 定义一个全局变量
gl_title = "黑马程序员"
# 在定义一个全局变量
gl_name = "小明"

def demo():

    print("%d" % gl_num)
    print("%s" % gl_title)
    print("%s" % gl_name)



demo()

