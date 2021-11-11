class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    def bark(self):
        print("叫得跟神一样...")


# 创建一个对象 - 狗对像
xtq = XiaoTianQuan()
# 如果子类中，重写了父类得方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()
