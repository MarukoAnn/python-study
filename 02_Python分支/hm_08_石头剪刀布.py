# 导入随机工具包
import random
# 从控制台输入要出的拳  - 石头(1) / 剪刀(2) / 布(3)
player = int(input("请输入您要出的拳头 石头(1) / 剪刀(2) / 布(3):"))
# 电脑随机出拳 —— 先假定 电脑只会出石头 ，完整的代码功能
computer = random.randint(1, 3)
print("玩家选择的拳头是 %d - 电脑出的拳是 %d" % (player, computer))
# 比较胜负
# 1、 石头 胜 剪刀
# 2、 剪刀 胜 布
# 3、 布 胜 石头
# if () or () or ():
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("欧耶，恭喜您胜利了")
# 平局
elif player == computer:
    print("真是心有灵犀呀,再来一次")
# 其他情况就是电脑获胜
else:
    print("很遗憾，你输了")
