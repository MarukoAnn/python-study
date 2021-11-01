# 记录所有的名片字典
card_list = []


def show_menu():
    """ 显示菜单 """
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("1、新增名片")
    print("2、显示全部")
    print("3、搜索名片")
    print("")
    print("0、退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("*" * 50)
    print("新增名片")

    # 1、提示用户输入名片详细信息
    name_str = input("清输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入邮箱：")
    # 2、提示用户输入的信息建立一个名片
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 3、将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 4、提示用户添加成功
    print("添加 %s 的名片成功!" % name_str)


def show_all():
    """显示所有名片"""
    print("*" * 50)
    print("显示所有名片")

    for label_text in ["姓名", "电话", "qq", "邮箱"]:
        print(label_text, end="\t\t")
    print("")
    # 打印分隔线
    print("=" * 50)

    # 遍历名片列表 依次输出字典信息
    for card_dist in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t"
              % (card_dist['name'],
                 card_dist['phone'],
                 card_dist['qq'],
                 card_dist['email']))


def search_card():
    """搜索名片"""
    print("*" * 50)
    print("搜索名片")