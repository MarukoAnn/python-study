import time


def sing():
    """唱歌"""
    for i in range(5):
        print("-----正在唱: 菊花茶------")
        time.sleep(1)


def dance():
    for i in range(5):
        print("-----正在跳舞------")
        time.sleep(1)


def main():
    sing()
    dance()
    pass


if __name__ == "__main__":

    main()