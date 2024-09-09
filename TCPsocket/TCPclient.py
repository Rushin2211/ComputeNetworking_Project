import socket
import time
import sys


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect(('172.31.100.218', 8888))

while True:
    data = input("客户端的信息: ")

    if data == 'quit':

        client_sock.close()

        time.sleep(1)

        sys.exit()

    elif not data:

        print("请重新输入数据")

        continue

    client_sock.send(data.encode('utf-8'))

    print("服务器的信息:", client_sock.recv(100000).upper().decode('utf-8'))

    print("")
