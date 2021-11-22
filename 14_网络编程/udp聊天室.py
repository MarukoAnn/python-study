import socket


def send_msg(udp_socket):
    dest_ip = input("目标ip：")
    dest_port = int(input("目标端口："))
    send_data = input("请输入需要发送内容：")
    # 发送消息
    udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    # print(recv_data)
    print("%s: %s" % (str(recv_data[1]), recv_data[0].decode("gbk")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定消息
    local_addr = ("", 7788)
    udp_socket.bind(local_addr)

    # 循环来进行处理事情
    while True:
        print("-------xxxx聊天齐----")
        print("1:发送消息")
        print("2:接收消息")
        print("0:退出系统")
        op = input("请输入功能：")

        if op == "1":
            # 发送
            send_msg(udp_socket)
        elif op == "2":
            # 接收并显示
            recv_msg(udp_socket)
        else:
            break


if __name__ == "__main__":
    main()


