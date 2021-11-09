class Women:

    def __init__(self, name):
        self.name = name
        self.__age = 18


    def __secret(self):
        # 在对象的方法内部, 是可以访问内部的私有属性的
        print("%s 的年龄 是%d" %(self.name, self.__age))


xiaofang = Women("小芳")
# 私有属性在外界不能直接被使用

# 在给属性 方法 命名时,实际上对名称做了一些特殊出来,使得外界无法访问
# 处理方式 在名称前加上_类名 => _类名__名称
# 在日常开发中,不要使用这种方式访问对象得私有属性和私有方法
print(xiaofang._Women__age)
#  私有方法 同样不能在外部直接调用
xiaofang._Women__secret()

#