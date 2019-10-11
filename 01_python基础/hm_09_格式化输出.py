# 定义字符串变量 name， 输出我的名字叫小明，请多多关照
name = "小明"
print("我的名字叫%s, 请多多关照" % name)
# 定义整数变量 student_no， 输出我的序号是 0001
student_no = 200
print("我的序号为%06d" % student_no)
# 定义小数 price、weight、money
# 输出 苹果单价9.00 元/斤，购买了 5.00 斤，需要支付45.00元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价%.2f元/斤,购买了%.2f斤，需要支付%.3f元"% (price, weight, money))

# 定义一个小数 scale, 输出 数据比例是10.00%
scale = 0.25
print("数据比例是 %.2f%%" % (scale * 100))