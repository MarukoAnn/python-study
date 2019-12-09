# 注意：定义好函数之后，之后表示这个函数封装一段代码而已
# 如果不主动调用函数，函数是不会主动执行的
name = "小明"

# say_hello()


def say_hello():
    """
     打招呼
    :return:
    """
    print("hello1")
    print("hello2")
    print("hello3")


print(name)

# 调用函数
# 只有在程序中，主动调用函数，才能让函数执行
say_hello()

print(name)
