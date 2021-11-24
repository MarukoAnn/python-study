import threading
import time


def test2():
    for i in range(5):
        print("----test2------%d" % i)
        time.sleep(1)
    # 如果创建Thread时执行的函数，运行结束意味着这个子线程结束了

def test1():
    for i in range(5):
        print("----test1------%d" % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    # 当调用Thread的时候，不会创建线程
    # 当调用Thread创建出来的实例对象 start 方法的时候
    # 才会创建线程以及让这个线程开始运行
    t1.start()
    t2.start()

    while True:
        print(threading.enumerate())
        time.sleep(1)

    pass


if __name__ == "__main__":
    main()