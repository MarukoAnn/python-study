import socket


def main():
    # 创建以恶搞udp 套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以使用socket 收发数据
    # udp_socket.sendto("hahaha", 对方得IP和端口)

    udp_socket.sendto(b"hahaha12", ("192.168.2.4", 8080))

    # 关闭套接字
    udp_socket.close()

    print('-----run-------')




if __name__ == "__main__":

    main()

