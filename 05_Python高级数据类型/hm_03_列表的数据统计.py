name_list = ["张三", "李四", "王五", "张三"]

# len(length 长度) 函数可以统计列表中元素的总数

name_len = len(name_list)

print("该列表的长度为%d" % name_len)


# count 方法可以统计列表中某一个数数出现的次数

name_times = name_list.count("张三")

print("张三出现了%d次" % name_times)

# 从列表中删除第一次出现的数据, 如果数据不存在, 程序会报错

name_list.remove("张三")

print(name_list)