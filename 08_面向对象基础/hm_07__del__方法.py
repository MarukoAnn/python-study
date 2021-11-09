class Cat:

    def __init__(self, name):
        # self.属性名 = 属性初始值
        self.name = name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s我去了" % self.name)


# tom 是一个全局变量
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象
del tom

print("-" * 50)