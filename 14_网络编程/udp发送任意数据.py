import socket


def main():
    # 创建以恶搞udp 套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 从键盘获取数据
    send_data = input("请输入需要发送的数据: ")
    # 可以使用socket 收发数据
    # udp_socket.sendto("hahaha", 对方得IP和端口)

    print("数据 ：%s" % send_data.encode("utf-8"))
    udp_socket.sendto(send_data.encode("utf-8"), ("10.10.23.45", 8080))

    # 关闭套接字
    udp_socket.close()

    print('-----run-------')




if __name__ == "__main__":

    main()

