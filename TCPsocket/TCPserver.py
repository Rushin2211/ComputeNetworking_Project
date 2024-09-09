import socket
import sys


def TCP(sock, address):

    print("已成功连接", address)

    while True:
        data = sock.recv(100000000)

        print("客户端的信息:", data.upper().decode('utf-8'))

        respond = input("服务器的信息:")

        if respond == 'quit':

            sock.close()

            time.sleep(1)
 
            sys.exit()

        print("")

        if data.decode == 'quit':

            print("连接已中断")

            break

        sock.send(respond.encode('utf-8'))

    sock.close()


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind(('172.31.100.218', 8888))

server_sock.listen(1)

print("正在等待连接......")

while True:
    sock, address = server_sock.accept()

    TCP(sock, address)
