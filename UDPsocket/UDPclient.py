import socket
import sys


client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('172.31.100.218', 888)

while True:
    data = input("请输入要发送的信息: ")

    if not data or data == 'quit':

        client_sock.close()

        sys.exit()

        break

    client_sock.sendto(data.encode('utf-8'), server_address)

    print("数据已发送到", server_address)

    respond, address = client_sock.recvfrom(10000)

    print("返回的信息为: ", respond.decode('utf-8'))

    print("")
