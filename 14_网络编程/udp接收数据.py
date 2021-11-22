import socket


def main():
    # 创建udp 套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定一个本地信息
    local_addr = ("", 7788)
    udp_socket.bind(local_addr)  # 必须绑定自己电脑的ip和端口

    while True:
        # 接收数据
        recv_message = udp_socket.recvfrom(1024) # 1024表示收到的最大字节数
        # recv_message 这个变量中存储的是一个元组(接受到的数据, (发送方的ip, port))
        recv_msg = recv_message[0]
        recv_addr = recv_message[1]
        # 打印收到的数据
        # print(recv_message)
        print("%s,%s" % (str(recv_addr), recv_msg.decode("gbk")))

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":

    main()

