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


class Cat(Animal):

    def catch(self):
        print("抓老鼠")


# 创建一个对象 - 狗对像
xtq = XiaoTianQuan()
cat = Cat()
xtq.run()
xtq.eat()
xtq.sleep()
cat.catch()
