class Cat:

    def __init__(self, name):
        print("这是一个初始化方法")
        # self.属性名 = 属性初始值
        self.name = name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名() 创建对象是 会自动调用初始化方法 __init__
tom = Cat("Tom1")

print(tom.name)