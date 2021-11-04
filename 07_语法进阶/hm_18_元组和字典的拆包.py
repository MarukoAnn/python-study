def demo(*args, **kwargs):

     print(args)
     print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dist = {'name': '小明', 'age': 18}
# 拆包语法 可以简化元组/字典变量的传递
demo(*gl_nums, **gl_dist)