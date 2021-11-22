import socket


def main():
    # 1、创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2、绑定本地信息
    tcp_socket.bind(("", 7780))

    # 3、让默认的套接字由主动变为被动 listen
    tcp_socket.listen(128)

    print("-----1-----")

    while True:
        print("等待一个新的客户端到来....")

        # 4、等待别人的电话到来(等待客户端的链接 accept)
        new_client_socker, client_addr = tcp_socket.accept()

        print("一个新的客户端已到来%s" % str(client_addr))

        print(client_addr)

        # 接收客户端发送过来的请求
        recv_data = new_client_socker.recv(1024)

        print("客户端发过来的请求是：%s" % recv_data)
        # 返回一些数据给客户端
        new_client_socker.send("哈哈哈哈".encode("gbk"))

        # 关闭套接字
        new_client_socker.close()

    tcp_socket.close()


if __name__ == "__main__":
    main()