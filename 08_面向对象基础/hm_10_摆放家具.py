class HomeItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):

        # Python能够自动将一对括号内部的代码链接在一起
        return ("户型：%s\n 总面积：%.2f【剩余：%.2f】\n家具：%s" %
                (self.house_type, self.area,
                 self.free_area, self.item_list))

    def add_item(self, item):

        # 1、 判断家具的面积
        if item.area > self.free_area:
            print("%s 面积太大了，无法添加" % item.name)

            return

        # 2、将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3、计算剩余面积
        self.free_area -= item.area


# 1、创建家具
bad = HomeItem("席梦思", 4)
chest = HomeItem("衣柜", 2)
table = HomeItem("餐桌", 1.5)
print(bad)
print(chest)
print(table)

# 创建房子
my_home = House("两室一厅", 60)
my_home.add_item(bad)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
