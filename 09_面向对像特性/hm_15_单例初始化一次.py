class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instence = None
    init_flag = False
    def __new__(cls, *args, **kwargs):
        # 1、判断类属性是否是空对象
        if cls.instence is None:
            # 2、调用父类的方法，为第一个对象分配空间
            cls.instence = super().__new__(cls)

        # 3、返回类属性保存的对象引用
        return cls.instence

    def __init__(self):

        # 1、判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 2、如果没有执行过，在执行初始化动作
        print("初始化完成")
        # 3、修改类属性标记
        MusicPlayer.init_flag = True

    pass


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
