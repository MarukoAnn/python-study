class A:

    def test(self):
        print("A的test方法")

    def demo(self):
        print("A的demo 方法")

class B:

    def test(self):
        print("B的test方法")

    def demo(self):
        print("B的demo 方法")


class C(A, B):
    """
    多继承可以让子类对象，同时具有多个父类的属性和方法
    """
    pass


# 创建子类对象
c = C()
print(C)

c.demo()
c.test()