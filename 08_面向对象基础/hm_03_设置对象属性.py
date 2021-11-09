class Cat:

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 爱喝水" % self.name)


# 创建猫对象
tom = Cat()

# 可以使用 .属性名 利用赋值语句就可以了
tom.name = "Tom"

tom.eat()
tom.drink()

lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
