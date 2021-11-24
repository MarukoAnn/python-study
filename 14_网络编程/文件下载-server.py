import socket


# 读取文件发送
def send_file_2_client(new_client_socket, client_addr):
    # 接收客户端发送过来的 要下载的文件名字
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)要下载的文件名为：%s" % (str(client_addr), file_name))
    file_content = None
    # 打开文件, 读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as result:
        print("没有要下载的文件(%s)：" % file_name)

    if file_content:
        # 发送文件数据给客户端
        new_client_socket.send(file_content)


def main():

    # 1、创建套接字
    tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2、绑定本地信息
    tcp_socket_server.bind(("", 7880))

    # 3、让套接字由主动变为被动listen
    tcp_socket_server.listen(128)

    while True:
        # 4、 等待客户端链接 accept
        new_client_socket, client_addr = tcp_socket_server.accept()

        # 发送文件
        send_file_2_client(new_client_socket, client_addr)

        # 7、关闭套接字
        new_client_socket.close()

    tcp_socket_server.close()


if __name__ == "__main__":
    main()
