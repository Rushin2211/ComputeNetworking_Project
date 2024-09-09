import socket
import random


server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_sock.bind(("", 8888))

while True:

    recv_data, client_addr = server_sock.recvfrom(10000)

    print("收到来自", client_addr, "的请求")

    rand = random.randint(0, 10)

    print(rand)

    if rand < 3:

        continue

    else:

        server_sock.sendto(recv_data.decode().upper().encode(), client_addr)
