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

        # 循环的目地：为同一个客户端 服务多次
        while True:
            # 接收客户端发送过来的请求
            recv_data = new_client_socker.recv(1024)

            print("客户端发过来的请求是：%s" % recv_data.decode("gbk"))
            # 判断客户端是否关闭链接，如果关闭链接，则接收到的值为 None
            # 如果recv解堵塞，有两种方式：
            # 1、客户端发送过来数据
            # 2、客户端调用close导致关闭，这里recv解堵塞
            if recv_data:
                # 返回一些数据给客户端
                new_client_socker.send("哈哈哈哈".encode("gbk"))
            else:
                break
        # 关闭套接字
        # 关闭accept返回的套接字 意味着 不会在为这个客户端服务
        new_client_socker.close()
        print("以及为这个客户端服务完毕....")
    # 如果将监听套接字关闭了，那么会导致 不能再次等待新客户端到来
    tcp_socket.close()


if __name__ == "__main__":
    main()