import socket


ProxyServer_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ProxyServer_sock.bind(('172.31.100.175', 1234))

ProxyServer_sock.listen(5)

while True:

    print("正在等待连接......")

    Client_sock, Client_addr = ProxyServer_sock.accept()

    ClientSend_message = Client_sock.recv(10000).decode()

    print("客户端发送的信息: ", ClientSend_message)

    FileName = ClientSend_message.split()[1].partition("//")[2].replace('/', '_')

    print("FileName: ", FileName)

    FileExist = "false"

    try:

        print("开始检查代理服务器中是否存在该文件: ", FileName)

        File = open(FileName, 'r')

        output_data = File.readlines()

        File.close()

        FileExist = "true"

        print("该文件存在在代理服务器中")

        for i in range(0, len(output_data)):

            Client_sock.send(output_data[i].encode())

    except IOError:

        if FileExist == "false":

            print("该文件不在代理服务器中，开始向远端服务器请求该文件")

            RemoteServer_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            RemoteServer_ip = ClientSend_message.split()[1].partition("//")[2].partition('/')[0]

            print("远端服务器IP地址: ", RemoteServer_ip)

            try:

                RemoteServer_sock.connect((RemoteServer_ip, 80))

                print("已连接到: ", RemoteServer_ip)

                RemoteServer_sock.sendall(ClientSend_message.encode())

                RemoteServerSend_message = RemoteServer_sock.recv(10000).decode()

                print("远端服务器返回的消息:\r\n", RemoteServerSend_message)

                Client_sock.sendall(RemoteServerSend_message.encode())

                NewFile = open("./" + FileName, 'w')

                NewFile.writelines(RemoteServerSend_message.replace('/r/n', '/n'))

                NewFile.close()

            except:

                print("向远端服务器请求文件失败")

    Client_sock.close()

ProxyServer_sock.close()
